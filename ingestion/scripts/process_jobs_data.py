import pandas as pd


df = pd.read_csv("data_lake/raw/data_sci_jobs.csv")


df = df.dropna()


df = df.drop_duplicates()


df.columns = df.columns.str.lower().str.replace(" ", "_")


df.to_csv("data_lake/processed/jobs_processed.csv", index=False)
print("Processed data saved successfully")