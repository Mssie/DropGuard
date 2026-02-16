DROP GUARD
AI-Powered Student Dropout Prediction & Intervention System

AgorAI Hackathon 2026 Submission

📌 Overview

Drop Guard is an AI-driven early warning system designed to predict student dropout risk using machine learning and explainable AI techniques.

The system analyzes academic performance, attendance patterns, psychosocial indicators, and home stability factors to:

Predict dropout probability

Explain the model’s decision using SHAP

Visualize academic progression

Generate personalized intervention plans

Provide downloadable AI-generated PDF reports

Enable school-level risk monitoring

This project bridges predictive intelligence with actionable educational intervention.

🎯 Problem Statement

Student dropout remains a critical global issue.
Educational institutions often lack:

Early predictive tools

Transparent AI explanations

Structured intervention guidance

Centralized risk dashboards

Drop Guard addresses these gaps through an interpretable AI pipeline designed for proactive decision-making.

🧠 System Architecture
Student Data
     ↓
Preprocessing Pipeline
     ↓
Feature Encoding
     ↓
Random Forest Model
     ↓
Risk Probability Output
     ↓
SHAP Explainability
     ↓
Intervention Engine
     ↓
Dashboard + PDF Report

🛠️ Technologies Used

Python

Scikit-learn (Random Forest Classifier)

SHAP (Explainable AI)

Gradio (Interactive Web Interface)

Plotly (Data Visualization)

ReportLab (PDF Generation)

Pandas / NumPy (Data Processing)

📊 Machine Learning Model
Model Type

Random Forest Classifier

Features Used

G1 (First-term grade)

G2 (Second-term grade)

Final grade

Number of past failures

Attendance rate

Mental health status

Internet access at home

Caregiver stability

Chronic illness

Target Variable

Binary classification:

0 → No Dropout Risk

1 → Dropout Risk

Why Random Forest?

Handles mixed feature types

Robust to overfitting

Strong baseline performance

Compatible with SHAP explainability

🔎 Explainability (SHAP Integration)

To avoid black-box predictions, Drop Guard integrates SHAP (SHapley Additive exPlanations).

This enables:

Feature impact ranking

Transparent risk contribution analysis

Trustworthy AI decision support

Each prediction includes a feature importance visualization highlighting the top risk drivers.

📈 Key Functionalities
1️⃣ Individual Student Risk Analysis

Risk percentage prediction

Risk level classification (Low / Medium / High)

Academic performance curve (G1 → G2 → Final)

SHAP feature importance chart

2️⃣ AI-Generated Intervention Plan

Automatically generated intervention strategy based on risk level.

3️⃣ PDF Report Export

Downloadable structured AI report including:

Risk score

Explanation

Recommended actions

4️⃣ Multi-Student Monitoring

Internal in-memory tracking of analyzed students for school-level oversight.

🗂️ Project Structure
drop-guard/
│
├── app.py
├── train_model.py
├── model/
│   └── dropout_model.pkl
├── data/
│   └── student_data.csv
├── utils/
│   ├── preprocess.py
│   ├── explain.py
│   └── report.py
├── requirements.txt
└── README.md

⚙️ Installation & Deployment
Option 1 — Local Run
pip install -r requirements.txt
python app.py

Option 2 — HuggingFace Spaces

Create new Gradio Space

Upload all files

Ensure dropout_model.pkl is included

Deploy

No additional configuration required.

📄 Dataset

The repository includes a structured student dataset (student_data.csv) used for model training.

For competition purposes, this dataset simulates realistic academic and socio-behavioral patterns.

Future versions may integrate real institutional data.

📌 Results & Impact

Drop Guard demonstrates:

Accurate dropout risk classification

Transparent AI decision reasoning

Actionable intervention recommendations

School-level risk visibility

The system enables educational institutions to shift from reactive responses to proactive prevention.

🔮 Future Improvements

Real-time semester monitoring

Cross-validation metrics dashboard

Confusion matrix & ROC curve visualization

Real database integration

Authentication & role-based access

LLM-powered counselor assistant

Institutional deployment

👩‍💻 Authors

AgorAI Hackathon 2026 Participant
Drop Guard Team

🏆 Vision

Drop Guard is not just a prediction tool —
it is an early intervention intelligence system designed to transform how educational institutions prevent student dropout.
