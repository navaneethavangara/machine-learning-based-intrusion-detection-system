# ==================================================
# K-MEANS CLUSTERING
# ==================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# --------------------------------------------------
# STEP 1: LOAD DATASET
# --------------------------------------------------

df = pd.read_csv("../dataset/KDDTrain+.txt", header=None)

# Select important features
# 4 -> src_bytes
# 5 -> dst_bytes

X = df[[4, 5]]

# --------------------------------------------------
# STEP 2: FEATURE SCALING
# --------------------------------------------------

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --------------------------------------------------
# STEP 3: APPLY K-MEANS
# --------------------------------------------------

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X_scaled)

labels = kmeans.labels_

# --------------------------------------------------
# STEP 4: TERMINAL OUTPUT
# --------------------------------------------------

print("======================================")
print("K-MEANS CLUSTERING RESULTS")
print("======================================\n")

print("Cluster Centers (Scaled Values):\n")
print(kmeans.cluster_centers_)

print("\nInertia (WCSS):", kmeans.inertia_)

# Cluster Distribution
unique, counts = np.unique(labels, return_counts=True)

print("\nCluster Distribution:")
for u, c in zip(unique, counts):
    print(f"Cluster {u}: {c} records")

# Identify anomaly cluster (smaller cluster)
anomaly_cluster = unique[np.argmin(counts)]
print("\nAnomaly Cluster Identified As:", anomaly_cluster)

print("\nInterpretation:")
print("Smaller cluster is treated as anomalous traffic.")
print("Larger cluster represents normal traffic.")

# --------------------------------------------------
# STEP 5: GRAPH VISUALIZATION
# --------------------------------------------------

# Separate normal and anomaly data
normal_data = df[labels != anomaly_cluster]
anomaly_data = df[labels == anomaly_cluster]

# Convert centroids back to original scale
centroids = scaler.inverse_transform(kmeans.cluster_centers_)

plt.figure(figsize=(8,6))

# Plot normal traffic
plt.scatter(
    normal_data[4],
    normal_data[5],
    label="Normal Traffic"
)

# Plot anomalous traffic
plt.scatter(
    anomaly_data[4],
    anomaly_data[5],
    label="Anomalous Traffic"
)

# Plot centroids
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker='X',
    s=250,
    label="Centroids"
)

plt.title("K-Means Based Intrusion Detection System")
plt.xlabel("Source Bytes")
plt.ylabel("Destination Bytes")
plt.legend()

plt.tight_layout()
plt.show()