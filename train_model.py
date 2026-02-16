import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from utils.preprocess import preprocess_data

df = pd.read_csv("data/student_data.csv")

X, y, le = preprocess_data(df)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X, y)

joblib.dump((model, le), "model/dropout_model.pkl")

print("Model trained and saved.")
