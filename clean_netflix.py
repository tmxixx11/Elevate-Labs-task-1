
import pandas as pd

df = pd.read_csv("netflix_titles.csv")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

initial_rows = len(df)

df = df.drop_duplicates()
df = df.drop_duplicates(subset=["show_id"])

text_columns = [
    "type", "title", "director", "cast",
    "country", "rating", "duration",
    "listed_in", "description"
]

for col in text_columns:
    df[col] = df[col].fillna("Unknown")
    df[col] = df[col].astype(str).str.strip()

df["type"] = df["type"].str.title()
df["rating"] = df["rating"].str.upper()

df["date_added"] = pd.to_datetime(
    df["date_added"].str.strip(),
    format="mixed",
    errors="coerce"
)

df["release_year"] = pd.to_numeric(
    df["release_year"], errors="coerce"
).astype("Int64")

df["date_added"] = df["date_added"].dt.strftime("%Y-%m-%d")
df["date_added"] = df["date_added"].fillna("Unknown")

df = df.replace(r"^\s*$", "Unknown", regex=True)

df.to_csv("netflix_cleaned.csv", index=False)

print("Original rows:", initial_rows)
print("Cleaned rows:", len(df))
print("Duplicates removed:", initial_rows - len(df))
print("Missing values after cleaning:")
print(df.isnull().sum())
print("Cleaned dataset saved successfully!")
