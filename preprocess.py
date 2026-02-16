import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    df = df.copy()

    le = LabelEncoder()
    df["Mental_Health"] = le.fit_transform(df["Mental_Health"])

    X = df.drop("Dropout", axis=1)
    y = df["Dropout"]

    return X, y, le
