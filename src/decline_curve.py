from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

data_path = Path("data/processed/volve_monthly_production_clean.csv")
figures_dir = Path("reports/figures")
figures_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(data_path)
df["date"] = pd.to_datetime(df["date"])

df = df[(df["oil_sm3"] > 0) & (df["on_stream_hrs"] > 0)].copy()
df = df.sort_values(["wellbore", "date"])

top_wells = (
    df.groupby("wellbore")["oil_sm3"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .index
)

results = []

for well in top_wells:
    wdf = df[df["wellbore"] == well].copy()

    peak_idx = wdf["oil_sm3"].idxmax()
    decline_df = wdf.loc[peak_idx:].copy()

    if len(decline_df) < 6:
        continue

    decline_df["t_months"] = np.arange(len(decline_df))
    decline_df["log_oil"] = np.log(decline_df["oil_sm3"])

    slope, intercept = np.polyfit(
        decline_df["t_months"],
        decline_df["log_oil"],
        1
    )

    decline_rate_monthly = -slope
    qi = np.exp(intercept)

    decline_df["predicted_oil_sm3"] = qi * np.exp(
        -decline_rate_monthly * decline_df["t_months"]
    )

    r2 = r2_score(decline_df["oil_sm3"], decline_df["predicted_oil_sm3"])
    annual_decline_percent = (1 - np.exp(-12 * decline_rate_monthly)) * 100

    results.append({
        "wellbore": well,
        "qi_sm3": round(qi, 2),
        "monthly_decline_rate": round(decline_rate_monthly, 5),
        "annual_decline_percent": round(annual_decline_percent, 2),
        "r2": round(r2, 4),
        "months_used": len(decline_df)
    })

    plt.figure(figsize=(10, 5))
    plt.plot(decline_df["date"], decline_df["oil_sm3"], label="Actual oil")
    plt.plot(decline_df["date"], decline_df["predicted_oil_sm3"], label="Exponential decline fit")
    plt.title(f"Decline Curve Analysis: {well}")
    plt.xlabel("Date")
    plt.ylabel("Oil production, Sm3")
    plt.legend()
    plt.tight_layout()

    safe_name = well.replace("/", "_").replace(" ", "_")
    plt.savefig(figures_dir / f"decline_curve_{safe_name}.png")
    plt.close()

results_df = pd.DataFrame(results)
results_path = Path("reports/decline_curve_results.csv")
results_df.to_csv(results_path, index=False)

print("Decline curve analysis completed.")
print(results_df)
print("Results saved to:", results_path)
print("Figures saved to:", figures_dir)
