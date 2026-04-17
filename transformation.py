import pandas as pd

INPUT = "data/raw/alumni.csv"
OUTPUT = "data/processed/alumni_cleaned.csv"

def transform():
    df = pd.read_csv(INPUT)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values
    df.fillna({
        "salary": df["salary"].mean(),
        "company": "Unknown"
    }, inplace=True)

    # Experience level
    df["experience_level"] = df["graduation_year"].apply(
        lambda x: "Senior" if x < 2020 else "Junior"
    )

    # Salary range
    df["salary_range"] = pd.cut(
        df["salary"],
        bins=[0, 600000, 1200000, 2000000],
        labels=["Low", "Medium", "High"]
    )

    df.to_csv(OUTPUT, index=False)
    print("Transformation Done!")

if __name__ == "__main__":
    transform()