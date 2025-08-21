import pandas as pd
import matplotlib.pyplot as plt

INPUT_CSV = "C:\\Users\\ASUS\\Downloads\\accidents.csv"
OUT_CSV = "accidents_with_metrics.csv"
OUT_PNG = "accident_trend.png"

df = pd.read_csv(INPUT_CSV)
df = df[["Year", "Accidents_No_Helmet"]]
df = df.sort_values("Year").reset_index(drop=True)

df["YoY_Change"] = df["Accidents_No_Helmet"].diff()
df["YoY_%"] = df["Accidents_No_Helmet"].pct_change() * 100
df["3yr_Rolling_Avg"] = df["Accidents_No_Helmet"].rolling(3, min_periods=1).mean().round(2)

df["Is_Peak"] = df["Accidents_No_Helmet"] == df["Accidents_No_Helmet"].max()
df["Is_Trough"] = df["Accidents_No_Helmet"] == df["Accidents_No_Helmet"].min()

df.to_csv(OUT_CSV, index=False)

plt.figure(figsize=(7, 4))
plt.plot(df["Year"], df["Accidents_No_Helmet"], marker="o")
plt.title("Accidents Attributed to No Helmet (Toy Data)")
plt.xlabel("Year")
plt.ylabel("Accident Count")
plt.grid(True, linestyle="--", linewidth=0.6, alpha=0.7)
plt.tight_layout()
plt.savefig(OUT_PNG, dpi=200)
plt.close()

peak = df.loc[df["Accidents_No_Helmet"].idxmax()]
trough = df.loc[df["Accidents_No_Helmet"].idxmin()]
print("=== Mini Literature Hunt: Toy Analysis Summary ===")
print(f"Years covered: {df['Year'].min()}–{df['Year'].max()}")
print(f"Peak year: {int(peak['Year'])} ({int(peak['Accidents_No_Helmet'])})")
print(f"Lowest year: {int(trough['Year'])} ({int(trough['Accidents_No_Helmet'])})")
print(f"Saved plot: {OUT_PNG}")
print(f"Saved metrics CSV: {OUT_CSV}")
