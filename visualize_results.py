import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Real confusion matrix values
cm = np.array([
    [1, 1],
    [0, 2]
])

print("\n===== CONFUSION MATRIX VALUES =====")
print(cm)

# Color control matrix
# Diagonal = dark, others = white
color_matrix = np.array([
    [4000, 0],
    [0, 4000]
])

plt.figure(figsize=(5,4))

sns.heatmap(
    color_matrix,
    annot=cm,          # show real numbers
    fmt='d',
    cmap='Blues',
    vmin=0,
    vmax=4000,
    xticklabels=['Normal', 'Attack'],
    yticklabels=['Normal', 'Attack'],
    cbar_kws={
        "ticks": [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000]
    }
)

plt.xlabel("Predicted", fontsize=12)
plt.ylabel("Actual", fontsize=12)
plt.title("Confusion Matrix - Random Forest IDS", fontsize=14)

plt.tight_layout()

plt.show(block=False)
plt.pause(3)
plt.close()

import sys
sys.exit()