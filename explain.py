import shap
import pandas as pd

def get_shap_values(model, input_df):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(input_df)[1][0]

    shap_df = pd.DataFrame({
        "Feature": input_df.columns,
        "Impact": shap_values
    }).sort_values(by="Impact", key=abs, ascending=False)

    return shap_df
