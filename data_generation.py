import numpy as np
import pandas as pd
import os

def generate_dataset(n=2000):
    np.random.seed(42)

    data = pd.DataFrame({
        "Student Name": [f"Student {i}" for i in range(n)],
        "Student ID": np.random.randint(1000, 9999, n),
        "Age": np.random.randint(15, 19, n),
        "Sex": np.random.choice(["Male","Female"], n),
        "Address": np.random.choice(["Rural","Urban","Suburban"], n),
        "Transport": np.random.choice(["Car","Bus","Bike","Walk"], n),
        "Device": np.random.choice(["None","Personal","Shared"], n),
        "Discipline": np.random.choice(["None","Occasional","Frequent"], n),
        "Employment": np.random.choice(["None","Part-time","Full-time"], n),
        "G1": np.random.randint(0,21,n),
        "G2": np.random.randint(0,21,n),
        "Final": np.random.randint(0,21,n),
        "Failures": np.random.randint(0,4,n),
        "Attendance Rate": np.random.randint(50,101,n),
        "Class Size": np.random.randint(20,41,n),
        "Participation": np.random.choice(["Low","Medium","High"], n),
        "Behavior Notes": np.random.choice([
            "Excellent leadership skills",
            "Frequently late, shows fatigue",
            "Disruptive occasionally",
            "Engaged in group work"
        ], n),
        "Living Arrangement": np.random.choice(["Both Parents","Relatives","Single Parent"], n),
        "Caregiver Stability": np.random.choice(["Stable","Unstable"], n),
        "No. of Siblings": np.random.randint(0,7,n),
        "Parents Status": np.random.choice(["Together","Apart"], n),
        "Mother Death Time": np.random.choice(["Not Applicable",">3 Years Ago"], n),
        "Father Death Time": np.random.choice(["Not Applicable",">3 Years Ago"], n),
        "Internet Home Access": np.random.choice([0,1], n),
        "Mother Education": np.random.choice(["Primary School","Secondary School","Higher Education"], n),
        "Mother Job": np.random.choice(["Unemployed","Private Sector","Public Sector"], n),
        "Father Education": np.random.choice(["Primary School","Secondary School","Higher Education"], n),
        "Father Job": np.random.choice(["Unemployed","Private Sector","Public Sector"], n),
        "Mental Health Status": np.random.choice(["None","Mild","Moderate","Severe"], n),
        "Chronic Illness": np.random.choice(["None","Heart Condition","Diabetes","Other"], n),
        "Special Needs": np.random.choice(["None","Autism Spectrum","Physical Disability"], n)
    })

    # Calculate dropout risk as numeric, then binary
    risk_score = (
        0.35*(100-data["Attendance Rate"]) +
        0.4*(20-data["Final"]) +
        2*data["No. of Siblings"] +
        1.5*(data["Caregiver Stability"]=="Unstable").astype(int)*10 +
        1.2*(data["Participation"].map({"Low":0,"Medium":5,"High":10})) +
        2*(data["Mental Health Status"].map({"None":0,"Mild":1,"Moderate":3,"Severe":5})) +
        (data["Special Needs"]!="None").astype(int)*3
    )

    data["dropout_risk"] = (risk_score > np.percentile(risk_score,60)).astype(int)

    os.makedirs("data", exist_ok=True)
    data.to_csv("data/student_data.csv", index=False)

    print("✅ Dataset generated successfully")

if __name__ == "__main__":
    generate_dataset()
