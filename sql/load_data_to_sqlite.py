
from pathlib import Path
import sqlite3
import pandas as pd

# Find the project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Define input and output paths
CSV_PATH = PROJECT_ROOT / "data" / "processed" / "online_retail_clean.csv"
DB_PATH = PROJECT_ROOT / "data" / "processed" / "online_retail.db"

# Check that the CSV file exists
if not CSV_PATH.exists():
    raise FileNotFoundError(f"CSV file not found: {CSV_PATH}")

# Load the cleaned data
df = pd.read_csv(CSV_PATH)

# Create the SQLite database and load the table
with sqlite3.connect(DB_PATH) as connection:
    df.to_sql(
        "online_retail",
        connection,
        if_exists="replace",
        index=False
    )

    # Verify the number of rows
    row_count = connection.execute(
        "SELECT COUNT(*) FROM online_retail"
    ).fetchone()[0]

print(f"Database created: {DB_PATH}")
print(f"Rows loaded: {row_count:,}")
print(f"Columns loaded: {len(df.columns)}")
print("Column names:", ", ".join(df.columns))
