import pandas as pd
import joblib
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("dataset/train.csv")

# Drop label for unsupervised learning
X = df.drop("label", axis=1)

# One-hot encode categorical features
X = pd.get_dummies(X)

# Train KMeans
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

# Save model
joblib.dump(kmeans, "models/kmeans.pkl")

print("✅ Unsupervised model trained and saved successfully")
