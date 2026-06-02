import zipfile
from pathlib import Path
import pandas as pd

raw_dir = Path("data/raw")
processed_dir = Path("data/processed")
processed_dir.mkdir(parents=True, exist_ok=True)

zip_files = list(raw_dir.glob("*.zip"))
if not zip_files:
    raise FileNotFoundError("No zip file found in data/raw")

zip_path = zip_files[0]
extract_dir = raw_dir / "extracted"
extract_dir.mkdir(exist_ok=True)

with zipfile.ZipFile(zip_path, "r") as z:
    z.extractall(extract_dir)

xlsx_files = list(extract_dir.glob("*.xlsx"))
if not xlsx_files:
    raise FileNotFoundError("No Excel file found after extraction")

xlsx_path = xlsx_files[0]

df = pd.read_excel(xlsx_path, sheet_name="Monthly Production Data")

# Remove unit row and empty rows
df = df[pd.to_numeric(df["Year"], errors="coerce").notna()].copy()

df = df.rename(columns={
    "Wellbore name": "wellbore",
    "NPDCode": "npd_code",
    "Year": "year",
    "Month": "month",
    "On Stream": "on_stream_hrs",
    "Oil": "oil_sm3",
    "Gas": "gas_sm3",
    "Water": "water_sm3",
    "GI": "gas_injection_sm3",
    "WI": "water_injection_sm3"
})

numeric_cols = [
    "npd_code", "year", "month", "on_stream_hrs",
    "oil_sm3", "gas_sm3", "water_sm3",
    "gas_injection_sm3", "water_injection_sm3"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["year"] = df["year"].astype(int)
df["month"] = df["month"].astype(int)

df["date"] = pd.to_datetime(
    df["year"].astype(str) + "-" + df["month"].astype(str) + "-01"
)

df = df.sort_values(["wellbore", "date"])

output_path = processed_dir / "volve_monthly_production_clean.csv"
df.to_csv(output_path, index=False)

print("Cleaned data saved to:", output_path)
print("Shape:", df.shape)
print(df.head())
