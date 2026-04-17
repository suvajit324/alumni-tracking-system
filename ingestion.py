import pandas as pd

def ingest():
    df = pd.read_csv("../data/raw/alumni.csv")
    print("Data Loaded:")
    print(df.head())

if __name__ == "__main__":
    ingest()