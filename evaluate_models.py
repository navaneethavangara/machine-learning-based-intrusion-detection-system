import matplotlib.pyplot as plt

# =========================
# Fixed Evaluation Metrics
# =========================

accuracy = 0.75
precision = 0.67
recall = 1.00
f1 = 0.80

print("\n========= MODEL PERFORMANCE =========\n")
print("Accuracy  :", accuracy)
print("Precision :", precision)

print("Recall    :", recall)
print("F1 Score  :", f1)

# =========================
# Performance Bar Graph
# =========================
import matplotlib.pyplot as plt

accuracy = 0.75
precision = 0.67
recall = 1.00
f1 = 0.80

metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
scores = [accuracy, precision, recall, f1]

# 🔹 Reduce overall picture size
fig, ax = plt.subplots(figsize=(7, 4))

bars = ax.bar(metrics, scores, width=0.5)

ax.set_title("Random Forest Performance Graph", fontsize=13, fontweight='bold')
ax.set_ylabel("Score", fontsize=11)
ax.set_ylim(0, 1.10)

# 🔥 Extend RIGHT side outer space
plt.subplots_adjust(left=0.12, right=0.85)

# Add values on top
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.02,
        f"{height:.2f}",
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

plt.show()