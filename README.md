# NVIDIA GPU Launch Impact on Stock Price

This project explores the relationship between NVIDIA's major consumer GPU launches (RTX 20, 30, 40, and 50 series) and the company's stock price behavior. Using an event-driven analysis approach, we examine stock price movement 5 months before and after each product launch to identify patterns in investor sentiment, volatility, and long-term impact.

---

## Repository Structure

```
analysis/
├── data/
│   ├── Nvidia_stock_data_full.csv            # Full historical stock data
│   └── Nvidia_GPU_Event_Analysis.csv         # Filtered dataset around GPU launches
├── notebook/
│   ├── NVIDIA_GPU_Launch_Stock_Analysis.ipynb  # Main notebook with analysis and visualizations
│   └── images/                               # Saved plots and charts
├── code/                                     # Python scripts (optional future utilities)
```

---

## 📈 Key Highlights

- Event-driven financial modeling across 4 major GPU launches:
  - 🟢 **RTX 20 (Aug 2018)**
  - 🔵 **RTX 30 (Sep 2020)**
  - 🟡 **RTX 40 (Sep 2022)**
  - 🔴 **RTX 50 (Jan 2025)**

- Analysis includes:
  - Calculation of average pre-launch stock prices
  - Visualization of price deviations post-launch
  - Cross-comparison of market behavior per generation

- Interprets each launch’s financial impact based on macro conditions, innovation level, and investor response

---

## 🔍 Interpretation Summary

- **RTX 50**: Highest volatility; possibly linked to overvaluation, DeepSeek R1 announcement, or hardware issues.
- **RTX 40**: Flat impact; market focus may have shifted to AI hardware like A100/H100.
- **RTX 30**: Strong positive trend; driven by crypto boom, pandemic demand, and scarcity.
- **RTX 20**: Initial dip followed by recovery; due to weak early adoption and excess 10-series inventory.

---

## 🔧 Tech Stack

- Python 🐍 (Pandas, Seaborn, Matplotlib)
- Jupyter Notebooks (.ipynb)
- Event-driven time series analysis

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). Dataset attribution belongs to the original uploader on Kaggle. This work is for educational and non-commercial use only.

---

## ⚠️ Disclaimer

This project is **not affiliated with NVIDIA**. All analysis is based on publicly available historical data and is provided **as-is** without warranty. This is not financial advice.

---

## 🤝 Contributions

Feel free to fork the repository, suggest improvements, or submit PRs. Ideas like comparing to S&P500 or analyzing trading volume spikes are welcome.
