import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Load dataset
data = pd.read_csv("sales_data.csv")

print(data)

# Features and target
X = data[['Month_Number']]
y = data['Sales']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
error = mean_absolute_error(y_test, predictions)

print("\nMean Absolute Error:")
print(error)

# Future prediction
future = [[13]]

future_prediction = model.predict(future)

print("\nPredicted Sales for Month 13:")
print(future_prediction[0])

# Graph
all_predictions = model.predict(X)

plt.scatter(X, y)

plt.plot(X, all_predictions)

plt.xlabel("Month Number")

plt.ylabel("Sales")

plt.title("Predictive Analytics Using Historical Data")

plt.show()
