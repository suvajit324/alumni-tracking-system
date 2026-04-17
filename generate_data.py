import pandas as pd
import random

names = ["Amit", "Riya", "Arjun", "Rahul", "Priya", "Sneha", "Karan", "Neha", "Vikram", "Anjali"]
degrees = ["BTech", "MTech"]
departments = ["CSE", "IT", "ECE"]
companies = ["TCS", "Infosys", "Google", "Amazon", "Wipro", "Microsoft"]
roles = ["Engineer", "Analyst", "SDE", "Developer"]
locations = ["Bangalore", "Pune", "Hyderabad", "Chennai", "Delhi"]

data = []

for i in range(1, 101):  # 100 rows
    data.append([
        i,
        random.choice(names),
        random.randint(2015, 2023),
        random.choice(degrees),
        random.choice(departments),
        random.choice(companies),
        random.choice(roles),
        random.randint(400000, 2000000),
        random.choice(locations)
    ])

df = pd.DataFrame(data, columns=[
    "alumni_id", "name", "graduation_year", "degree",
    "department", "company", "job_role", "salary", "location"
])

df.to_csv("data/raw/alumni.csv", index=False)

print("✅ 100 rows generated successfully!")