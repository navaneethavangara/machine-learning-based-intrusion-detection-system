import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "train.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "supervised_model.pkl")
FEATURE_COLUMNS_PATH = os.path.join(BASE_DIR, "models", "feature_columns.pkl")

print("Loading dataset from:", DATA_PATH)

# Load dataset
data = pd.read_csv(DATA_PATH)

# Check label
if 'label' not in data.columns:
    raise Exception("Dataset must contain 'label' column")

# Split features and label
X = data.drop("label", axis=1)
y = data["label"]

print("Encoding categorical features using get_dummies...")

# Convert categorical → numeric safely
X = pd.get_dummies(X)

# Save feature columns
joblib.dump(X.columns.tolist(), FEATURE_COLUMNS_PATH)

print("Splitting dataset...")

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("Training Random Forest...")

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

print("Evaluating model...")

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save model
joblib.dump(model, MODEL_PATH)

print("\nSUCCESS")
print("Model saved at:", MODEL_PATH)
print("Feature columns saved at:", FEATURE_COLUMNS_PATH)
