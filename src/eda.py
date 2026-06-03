from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

data_path = Path("data/processed/volve_monthly_production_clean.csv")
figures_dir = Path("reports/figures")
figures_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(data_path)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["wellbore", "date"])

# 1. Oil production trend by wellbore
plt.figure(figsize=(11, 6))
for well in df["wellbore"].dropna().unique():
    wdf = df[df["wellbore"] == well]
    plt.plot(wdf["date"], wdf["oil_sm3"], label=well)

plt.title("Monthly Oil Production by Wellbore")
plt.xlabel("Date")
plt.ylabel("Oil production, Sm3")
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig(figures_dir / "monthly_oil_production_by_wellbore.png", dpi=160)
plt.close()

# 2. Cumulative oil production by wellbore
df["cumulative_oil_sm3"] = df.groupby("wellbore")["oil_sm3"].cumsum()

plt.figure(figsize=(11, 6))
for well in df["wellbore"].dropna().unique():
    wdf = df[df["wellbore"] == well]
    plt.plot(wdf["date"], wdf["cumulative_oil_sm3"], label=well)

plt.title("Cumulative Oil Production by Wellbore")
plt.xlabel("Date")
plt.ylabel("Cumulative oil production, Sm3")
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig(figures_dir / "cumulative_oil_production_by_wellbore.png", dpi=160)
plt.close()

# 3. Top wells by total oil production
top_oil = df.groupby("wellbore")["oil_sm3"].sum().sort_values(ascending=False)

plt.figure(figsize=(9, 5))
top_oil.plot(kind="bar")
plt.title("Total Oil Production by Wellbore")
plt.xlabel("Wellbore")
plt.ylabel("Total oil production, Sm3")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(figures_dir / "total_oil_production_by_wellbore.png", dpi=160)
plt.close()

# 4. Oil and water production over time
monthly_total = df.groupby("date")[["oil_sm3", "water_sm3"]].sum()

plt.figure(figsize=(11, 6))
plt.plot(monthly_total.index, monthly_total["oil_sm3"], label="Oil")
plt.plot(monthly_total.index, monthly_total["water_sm3"], label="Water")
plt.title("Total Oil vs Water Production Over Time")
plt.xlabel("Date")
plt.ylabel("Production, Sm3")
plt.legend()
plt.tight_layout()
plt.savefig(figures_dir / "oil_vs_water_production_over_time.png", dpi=160)
plt.close()

# 5. Average water cut by wellbore
df["water_cut"] = df["water_sm3"] / (df["oil_sm3"] + df["water_sm3"])
water_cut = df.groupby("wellbore")["water_cut"].mean().sort_values(ascending=False)

plt.figure(figsize=(9, 5))
water_cut.plot(kind="bar")
plt.title("Average Water Cut by Wellbore")
plt.xlabel("Wellbore")
plt.ylabel("Average water cut")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(figures_dir / "average_water_cut_by_wellbore.png", dpi=160)
plt.close()

print("EDA figures saved to reports/figures/")
