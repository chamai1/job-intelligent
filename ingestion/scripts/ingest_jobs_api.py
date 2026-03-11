import requests
import json

url = "https://remotive.com/api/remote-jobs"

response = requests.get(url)

data = response.json()

with open("../../data_lake/raw/jobs_api.json", "w") as f:
    json.dump(data, f)

print("Jobs API data saved successfully")