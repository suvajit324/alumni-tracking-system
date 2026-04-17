import pandas as pd
from sqlalchemy import create_engine

# Create SQLite connection (this will create alumni.db automatically)
engine = create_engine("sqlite:///alumni.db")

# Path to cleaned data
FILE_PATH = "data/processed/alumni_cleaned.csv"
def load():
    print("Loading cleaned data...")

    # Read cleaned CSV
    df = pd.read_csv(FILE_PATH)

    print("Data preview:")
    print(df.head())

    # Load into SQLite database
    df.to_sql(
        name="alumni",        # Table name
        con=engine,
        if_exists="replace",  # Replace table each time (safe for project)
        index=False
    )

    print("\n✅ Data successfully loaded into SQLite database (alumni.db)")

if __name__ == "__main__":
    load()