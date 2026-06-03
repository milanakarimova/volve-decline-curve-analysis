import sqlite3
from pathlib import Path
import pandas as pd

data_path = Path("data/processed/volve_monthly_production_clean.csv")
output_dir = Path("reports/sql_results")
output_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(data_path)

conn = sqlite3.connect(":memory:")
df.to_sql("volve_production", conn, index=False, if_exists="replace")

queries = {
    "well_production_summary": Path("sql/well_production_summary.sql"),
    "yearly_well_production": Path("sql/yearly_well_production.sql"),
}

for name, query_path in queries.items():
    query = query_path.read_text(encoding="utf-8")
    result = pd.read_sql_query(query, conn)
    result.to_csv(output_dir / f"{name}.csv", index=False)

    print(f"\n{name}")
    print(result.head(10))

conn.close()
print("\nSQL results saved to reports/sql_results/")
