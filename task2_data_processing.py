import json
import pandas as pd

# Load JSON file
with open("data/trends_20260401.json", "r") as f:
    data = json.load(f)
# Convert to DataFrame
df = pd.DataFrame(data)
# Remove duplicates
df = df.drop_duplicates(subset=["post_id"])
# Fill missing values
df["author"] = df["author"].fillna("unknown")
df["title"] = df["title"].fillna("no title")
# Convert numeric fields
df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0)
df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce").fillna(0)
# Save cleaned data
df.to_csv("data/cleaned_trends.csv", index=False)
print("Cleaned data saved as CSV")