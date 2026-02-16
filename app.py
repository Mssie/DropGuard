import gradio as gr
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px
from utils.explain import get_shap_values
from utils.report import generate_pdf

# Load trained model
model, le = joblib.load("model/dropout_model.pkl")

students_db = []

def analyze(name,G1,G2,Final,Failures,Attendance,Mental,Internet,Caregiver,Chronic):

    mh_encoded = le.transform([Mental])[0]

    input_df = pd.DataFrame([[
        G1,G2,Final,Failures,Attendance,
        mh_encoded,Internet,Caregiver,Chronic
    ]], columns=[
        "G1","G2","Final","Failures","Attendance",
        "Mental_Health","Internet",
        "Caregiver_Stability","Chronic_Illness"
    ])

    prob = model.predict_proba(input_df)[0][1]
    risk = round(prob*100,2)

    students_db.append({"Name":name,"Risk":risk})

    level = "LOW"
    if risk > 65:
        level = "HIGH"
    elif risk > 35:
        level = "MEDIUM"

    explanation = f"The model predicts {level} dropout risk based primarily on academic trajectory and attendance patterns."

    plan = "Intensive academic recovery and counselor intervention required." if level=="HIGH" else \
           "Structured mentoring and monitoring recommended." if level=="MEDIUM" else \
           "Maintain performance and periodic check-ins."

    shap_df = get_shap_values(model, input_df)
    shap_plot = px.bar(shap_df.head(5), x="Impact", y="Feature", orientation="h", template="plotly_dark")

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk,
        title={'text': "Dropout Risk %"},
        gauge={'axis': {'range': [0,100]}}
    ))

    curve = go.Figure()
    curve.add_trace(go.Scatter(x=["G1","G2","Final"], y=[G1,G2,Final], mode="lines+markers"))
    curve.update_layout(template="plotly_dark", yaxis=dict(range=[0,20]))

    pdf = generate_pdf(name,risk,explanation,plan)

    return gauge, shap_plot, curve, explanation, plan, pdf

with gr.Blocks() as demo:

    gr.Markdown("DROP GUARD — AI Dropout Intelligence System")

    name = gr.Textbox(label="Student Name")
    G1 = gr.Slider(0,20,label="G1")
    G2 = gr.Slider(0,20,label="G2")
    Final = gr.Slider(0,20,label="Final")
    Failures = gr.Slider(0,3,label="Failures")
    Attendance = gr.Slider(50,100,label="Attendance")
    Mental = gr.Dropdown(["Good","Moderate","Poor","Critical"])
    Internet = gr.Radio([0,1],label="Internet")
    Caregiver = gr.Radio([0,1],label="Caregiver Stability")
    Chronic = gr.Radio([0,1],label="Chronic Illness")

    btn = gr.Button("Analyze")

    gauge = gr.Plot()
    shap_plot = gr.Plot()
    curve = gr.Plot()
    explanation = gr.Textbox()
    plan = gr.Textbox()
    pdf = gr.File()

    btn.click(analyze,
              inputs=[name,G1,G2,Final,Failures,Attendance,Mental,Internet,Caregiver,Chronic],
              outputs=[gauge,shap_plot,curve,explanation,plan,pdf])

demo.launch()


