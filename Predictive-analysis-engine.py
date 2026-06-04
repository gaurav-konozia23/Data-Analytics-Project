import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Experience": [1, 2, 3, 4, 5, 6],
    "Salary": [25000, 35000, 45000, 55000, 65000, 75000]
}

df = pd.DataFrame(data)

X = df[["Experience"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[7]])

print("Predicted Salary:", prediction[0])
