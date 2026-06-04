import pandas as pd

# ---------------------------------------
# Customer Behavior Analysis System
# Author: Gaurav Verma
# ---------------------------------------

customer_data = {
    "Customer_ID": [101, 102, 103, 104, 105],
    "Age": [22, 35, 28, 45, 31],
    "Purchase_Amount": [5000, 12000, 8000, 15000, 9500],
    "Visits_Per_Month": [4, 8, 5, 10, 6]
}

df = pd.DataFrame(customer_data)

print("=" * 50)
print("      CUSTOMER BEHAVIOR ANALYSIS")
print("=" * 50)

print("\nCustomer Dataset:")
print(df)

# KPIs
avg_purchase = df["Purchase_Amount"].mean()
total_revenue = df["Purchase_Amount"].sum()
avg_visits = df["Visits_Per_Month"].mean()

top_customer = df.loc[
    df["Purchase_Amount"].idxmax(),
    "Customer_ID"
]

print("\n===== BUSINESS INSIGHTS =====")

print(f"Total Revenue: ₹{total_revenue:,}")
print(f"Average Purchase Amount: ₹{avg_purchase:,.2f}")
print(f"Average Monthly Visits: {avg_visits:.2f}")
print(f"Top Customer ID: {top_customer}")

print("\n===== CUSTOMER SEGMENTATION =====")

for _, row in df.iterrows():

    if row["Purchase_Amount"] >= 12000:
        category = "Premium Customer"

    elif row["Purchase_Amount"] >= 8000:
        category = "Regular Customer"

    else:
        category = "Basic Customer"

    print(
        f"Customer {row['Customer_ID']} -> {category}"
    )

print("\nAnalysis Completed Successfully.")
