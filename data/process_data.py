import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

files = list(DATA_DIR.glob("*.csv"))

dfs = []
for f in files:
    df = pd.read_csv(f)
    dfs.append(df)

data = pd.concat(dfs, ignore_index=True)

# Normalize product names so filtering is case-insensitive
data["product"] = data["product"].str.lower().str.strip()

# Keep only Pink Morsel
data = data[data["product"] == "pink morsel"]

# Clean currency strings and compute sales
data["price"] = data["price"].replace("[$,]", "", regex=True).astype(float)
data["quantity"] = pd.to_numeric(data["quantity"], errors="coerce")
data = data.dropna(subset=["price", "quantity"])
data["Sales"] = data["quantity"] * data["price"]

# Keep required fields only
final = data[["Sales", "date", "region"]]

# Rename for output format
final.columns = ["Sales", "Date", "Region"]

# Save output
final.to_csv(DATA_DIR / "formatted_sales.csv", index=False)

print("Saved formatted_sales.csv with", len(final), "rows")
