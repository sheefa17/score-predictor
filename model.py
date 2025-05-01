import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Simple dataset: Hours vs Scores
data = {
    "Hours": [1, 2, 3, 4, 5],
    "Scores": [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

X = df[['Hours']]  # Feature
y = df['Scores']   # Target

model = LinearRegression()
model.fit(X, y)

# Save the correct model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Correct Score Predictor model trained and saved as model.pkl")

