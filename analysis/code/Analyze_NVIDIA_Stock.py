import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

df = pd.read_csv("Nvidia_stock_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

launch_dates = {
    "RTX 20": datetime(2018, 8, 20),
    "RTX 30": datetime(2020, 9, 1),
    "RTX 40": datetime(2022, 9, 20),
    "RTX 50": datetime(2025, 1, 6)
}

five_months = timedelta(days=150)
filtered = []

for series, launch in launch_dates.items():
    temp_df = df[(df['Date'] >= launch - five_months) & (df['Date'] <= launch + five_months)].copy()
    temp_df['Series'] = series
    temp_df['Phase'] = temp_df['Date'].apply(lambda x: 'Pre-launch' if x < launch else 'Post-launch')
    temp_df['Days_From_Launch'] = (temp_df['Date'] - launch).dt.days

    pre_avg = temp_df[temp_df['Phase'] == 'Pre-launch']['Close'].mean()

    temp_df['Close_Diff'] = temp_df['Close'] - pre_avg

    filtered.append(temp_df)

final_df = pd.concat(filtered).reset_index(drop=True)

sns.set(style="whitegrid")
plt.figure(figsize=(14, 6))
sns.lineplot(data=final_df, x="Days_From_Launch", y="Close_Diff", hue="Series", style="Phase")
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.title("NVIDIA GPU Series: Price Change Relative to Pre-launch Average")
plt.xlabel("Days from Launch (Negative = Pre, Positive = Post)")
plt.ylabel("Close - Pre-launch Avg Close")
plt.tight_layout()
plt.show()
