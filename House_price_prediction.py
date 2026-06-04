import pandas as pd
from sklearn.linear_model import LinearRegression

# -----------------------------------
# House Price Prediction System
# Author: Gaurav Verma
# -----------------------------------

housing_data = {
    "Area_sqft": [800, 1000, 1200, 1500, 1800, 2000, 2500],
    "Bedrooms": [2, 2, 3, 3, 4, 4, 5],
    "Price": [3500000, 4500000, 5500000, 7000000, 8500000, 9500000, 12000000]
}

df = pd.DataFrame(housing_data)

print("========== HOUSING DATA ==========")
print(df)

# Features and Target
X = df[["Area_sqft", "Bedrooms"]]
y = df["Price"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Prediction
new_house = [[1600, 3]]

predicted_price = model.predict(new_house)

print("\n========== PREDICTION ==========")
print(f"Area: {new_house[0][0]} sqft")
print(f"Bedrooms: {new_house[0][1]}")
print(f"Estimated Price: ₹{predicted_price[0]:,.2f}")

print("\nModel Training Completed Successfully")
