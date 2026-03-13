import pandas as pd

df = pd.read_csv("data_lake/processed/jobs_processed.csv")

skills_list = [
    "python",
    "sql",
    "power bi",
    "tableau",
    "excel",
    "machine learning",
    "data analysis"
]

def extract_skills(text):
    text = str(text).lower()
    found = [skill for skill in skills_list if skill in text]
    return ", ".join(found)

# استخراج skills من job_title
df["skills"] = df["job_title"].apply(extract_skills)

df.to_csv("data_lake/curated/jobs_with_skills.csv", index=False)

print("Skills extraction completed successfully")