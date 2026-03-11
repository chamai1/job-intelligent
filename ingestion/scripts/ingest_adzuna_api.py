import requests
import json

APP_ID = "466bb258"
APP_KEY = "24de3f25fc392cd7d4ddd57860050a94"

url = f"https://api.adzuna.com/v1/api/jobs/us/search/1?app_id={APP_ID}&app_key={APP_KEY}&what=data"

response = requests.get(url)

data = response.json()

with open("../../data_lake/raw/jobs_adzuna.json", "w") as f:
    json.dump(data, f)

print("Adzuna jobs data saved successfully")