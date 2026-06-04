import pandas as pd

# -----------------------------
# Sales Analytics Dashboard
# Author: Gaurav Verma
# -----------------------------

sales_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 18000, 22000, 25000, 28000],
    "Expenses": [7000, 8000, 9500, 11000, 12500, 14000]
}

df = pd.DataFrame(sales_data)

# Profit Calculation
df["Profit"] = df["Sales"] - df["Expenses"]

# Growth Rate
df["Growth %"] = df["Sales"].pct_change() * 100

print("=" * 50)
print("        SALES ANALYTICS REPORT")
print("=" * 50)

print("\nDataset:")
print(df)

print("\nKey Performance Indicators (KPIs)")
print("-" * 50)

print(f"Total Sales      : ₹{df['Sales'].sum():,}")
print(f"Total Expenses   : ₹{df['Expenses'].sum():,}")
print(f"Total Profit     : ₹{df['Profit'].sum():,}")

print(f"\nAverage Monthly Sales : ₹{df['Sales'].mean():,.2f}")
print(f"Average Profit        : ₹{df['Profit'].mean():,.2f}")

best_month = df.loc[df["Profit"].idxmax(), "Month"]
best_profit = df["Profit"].max()

print(f"\nBest Performing Month : {best_month}")
print(f"Highest Profit        : ₹{best_profit:,}")

print("\nMonthly Profit Report")
print("-" * 50)

for _, row in df.iterrows():
    print(
        f"{row['Month']} | "
        f"Sales: ₹{row['Sales']:,} | "
        f"Profit: ₹{row['Profit']:,}"
    )

print("\nAnalysis Completed Successfully.")
