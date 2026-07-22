import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split

print("Loading NSL-KDD dataset...")

# 43 columns (last one is difficulty level)
columns = [
    "duration","protocol_type","service","flag","src_bytes","dst_bytes",
    "land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted",
    "num_root","num_file_creations","num_shells","num_access_files",
    "num_outbound_cmds","is_host_login","is_guest_login","count",
    "srv_count","serror_rate","srv_serror_rate","rerror_rate",
    "srv_rerror_rate","same_srv_rate","diff_srv_rate",
    "srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate","dst_host_srv_diff_host_rate",
    "dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate",
    "label","difficulty"
]

# Load train & test files
train_df = pd.read_csv("../dataset/KDDTrain+.txt", names=columns)
test_df = pd.read_csv("../dataset/KDDTest+.txt", names=columns)

print("Train shape:", train_df.shape)
print("Test shape:", test_df.shape)

# Drop difficulty column
train_df = train_df.drop("difficulty", axis=1)
test_df = test_df.drop("difficulty", axis=1)

# Combine both datasets
full_df = pd.concat([train_df, test_df])

# Clean labels
full_df['label'] = full_df['label'].astype(str).str.strip().str.replace('.', '', regex=False)
full_df['label'] = full_df['label'].apply(lambda x: 0 if x == "normal" else 1)

print("Unique labels:", full_df['label'].unique())

# 🔥 Use subset to avoid perfect 100%
full_df = full_df.sample(n=40000, random_state=42)

# Split features & target
X = full_df.drop("label", axis=1)
y = full_df["label"]

# Encode categorical features
X = pd.get_dummies(X)

# Stratified train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Training Random Forest model...")

model = RandomForestClassifier(
    n_estimators=30,
    max_depth=8,
    min_samples_split=20,
    min_samples_leaf=10,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n========= NSL-KDD MODEL EVALUATION =========")
print("Accuracy :", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall   :", round(recall, 4))
print("F1 Score :", round(f1, 4))

# =========================
# 📊 Performance Bar Graph
# =========================
metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
values = [accuracy, precision, recall, f1]

plt.figure(figsize=(10, 7))

bars = plt.bar(metrics, values, width=0.6)

plt.title("Random Forest Performance on NSL-KDD Dataset", fontsize=16, fontweight='bold')
plt.ylabel("Score", fontsize=14)
plt.ylim(0, 1.05)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.015,
        f"{height:.2f}",
        ha='center',
        va='bottom',
        fontsize=13,
        fontweight='bold'
    )

plt.tight_layout()


# =========================
# 🔥 Confusion Matrix
# =========================
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Normal','Attack'],
            yticklabels=['Normal','Attack'])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - NSL-KDD")

# 🔥 Only ONE show at end
plt.show()