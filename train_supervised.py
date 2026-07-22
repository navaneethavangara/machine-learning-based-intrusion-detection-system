import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("dataset/train.csv")

# Separate label
y = df["label"]
X = df.drop("label", axis=1)

# One-hot encode categorical columns
X = pd.get_dummies(X)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model and columns
joblib.dump(model, "models/random_forest.pkl")
joblib.dump(X.columns.tolist(), "models/feature_columns.pkl")

print("✅ Supervised model trained and saved successfully")
