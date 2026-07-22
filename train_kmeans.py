# ===============================
# KMEANS GRAPH FOR IDS PROJECT
# ===============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import sys

print("========== KMEANS SCRIPT STARTED ==========")

# ===============================
# 1. LOAD DATASET
# ===============================

try:
    data = pd.read_csv("network_data.csv")
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading dataset:", e)
    sys.exit()

# Check required columns
if 'source_bytes' not in data.columns or 'destination_bytes' not in data.columns:
    print("Required columns not found in dataset!")
    sys.exit()

X = data[['source_bytes', 'destination_bytes']]
print("Total Samples:", len(X))

# ===============================
# 2. SCALE FEATURES
# ===============================

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Data scaling completed.")

# ===============================
# 3. APPLY KMEANS
# ===============================

kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

print("Clustering completed.")

# ===============================
# 4. TERMINAL OUTPUT
# ===============================

print("\n========== K-MEANS EVALUATION ==========")

# Cluster distribution
unique, counts = np.unique(clusters, return_counts=True)
for u, c in zip(unique, counts):
    print(f"Cluster {u}: {c} samples")

# Inertia
print("\nInertia (SSE):", round(kmeans.inertia_, 4))

# Silhouette Score
score = silhouette_score(X_scaled, clusters)
print("Silhouette Score:", round(score, 4))

print("=========================================\n")

# ===============================
# 5. PLOT GRAPH
# ===============================

plt.figure(figsize=(8, 6))

plt.scatter(
    X['source_bytes'],
    X['destination_bytes'],
    c=clusters,
    cmap='viridis',
    s=50
)

plt.title("K-Means Clustering for Intrusion Detection")
plt.xlabel("Source Bytes")
plt.ylabel("Destination Bytes")
plt.colorbar(label="Cluster")

plt.tight_layout()
plt.show()

print("========== SCRIPT FINISHED ==========")
