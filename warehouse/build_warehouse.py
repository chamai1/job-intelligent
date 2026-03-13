import pandas as pd
import os

# قراءة curated data
df = pd.read_csv("data_lake/curated/jobs_with_skills.csv")

# إنشاء folder output
os.makedirs("warehouse/output", exist_ok=True)

# -------------------------
# dim_company
# -------------------------
dim_company = df[["company"]].drop_duplicates().reset_index(drop=True)
dim_company["company_id"] = dim_company.index + 1
dim_company = dim_company[["company_id", "company"]]

# -------------------------
# dim_location
# -------------------------
dim_location = df[["location"]].drop_duplicates().reset_index(drop=True)
dim_location["location_id"] = dim_location.index + 1
dim_location = dim_location[["location_id", "location"]]

# -------------------------
# dim_skills
# -------------------------
all_skills = (
    df["skills"]
    .fillna("")
    .str.split(",")
    .explode()
    .str.strip()
)
all_skills = all_skills[all_skills != ""].drop_duplicates().reset_index(drop=True)

dim_skills = pd.DataFrame({"skill": all_skills})
dim_skills["skill_id"] = dim_skills.index + 1
dim_skills = dim_skills[["skill_id", "skill"]]

# -------------------------
# fact_jobs
# -------------------------
fact_jobs = df.copy()

# ربط company_id
fact_jobs = fact_jobs.merge(dim_company, on="company", how="left")

# ربط location_id
fact_jobs = fact_jobs.merge(dim_location, on="location", how="left")

# job_id
fact_jobs["job_id"] = range(1, len(fact_jobs) + 1)

# اختيار الأعمدة المهمة
fact_jobs = fact_jobs[
    ["job_id", "job_title", "estimated_salary", "company_id", "location_id", "skills"]
]

# -------------------------
# حفظ الجداول
# -------------------------
dim_company.to_csv("warehouse/output/dim_company.csv", index=False)
dim_location.to_csv("warehouse/output/dim_location.csv", index=False)
dim_skills.to_csv("warehouse/output/dim_skills.csv", index=False)
fact_jobs.to_csv("warehouse/output/fact_jobs.csv", index=False)

print("Data warehouse tables created successfully")