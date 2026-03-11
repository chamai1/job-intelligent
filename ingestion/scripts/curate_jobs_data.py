import pandas as pd


df = pd.read_csv("data_lake/processed/jobs_processed.csv")


columns_needed = ["job_title", "company", "location"]


df_curated = df[columns_needed]

df_curated.to_csv("data_lake/curated/jobs_curated.csv", index=False)

print("Curated dataset ready")