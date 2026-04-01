import json
import pandas as pd

# Load JSON file # Load JSON file from data folder
with open("data/trends_20260401.json", "r") as f:
    data = json.load(f)
# Convert to DataFrame
# Convert JSON data into DataFrame
df = pd.DataFrame(data)
# Remove duplicates
# Remove duplicate posts based on post_id
df = df.drop_duplicates(subset=["post_id"])
# Fill missing values
# Fill missing values in important columns
df["author"] = df["author"].fillna("unknown")
df["title"] = df["title"].fillna("no title")
# Convert numeric fields
# Convert score and num_comments to numeric values
df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0)
df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce").fillna(0)
# Save cleaned data
# Save cleaned data as CSV file
df.to_csv("data/cleaned_trends.csv", index=False)
print("Cleaned data saved as CSV")
