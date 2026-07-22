import pandas as pd
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans

print("Loading dataset...")

dataset_path = os.path.join(os.path.dirname(__file__), "dataset", "train.csv")

print("Looking for dataset at:", dataset_path)

# SAFE loader for corrupted CSV files
df = pd.read_csv(
    dataset_path,
    sep=",",
    engine="python",
    on_bad_lines="skip",   # skips corrupted lines
    skip_blank_lines=True
)

print("Dataset loaded successfully")
print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())

# Separate features and label
X = df.drop("label", axis=1)
y = df["label"]

# Convert categorical features
X = pd.get_dummies(X)

print("Features shape after encoding:", X.shape)

# Create models folder
models_path = os.path.join(os.path.dirname(__file__), "..", "models")
os.makedirs(models_path, exist_ok=True)

# Save feature columns
with open(os.path.join(models_path, "feature_columns.pkl"), "wb") as f:
    pickle.dump(X.columns, f)

# Train Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, y)

with open(os.path.join(models_path, "random_forest.pkl"), "wb") as f:
    pickle.dump(rf, f)

print("Random Forest model saved")

# Train KMeans
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

with open(os.path.join(models_path, "kmeans.pkl"), "wb") as f:
    pickle.dump(kmeans, f)

print("KMeans model saved")

print("Training completed successfully")