import joblib
import numpy as np
from database import insert_log

rf = joblib.load("models/random_forest.pkl")
km = joblib.load("models/kmeans.pkl")

def predict_intrusion(features):
    data = np.array(features).reshape(1, -1)

    rf_pred = rf.predict(data)[0]
    km_pred = km.predict(data)[0]

    rf_result = "Attack" if rf_pred == 1 else "Normal"

    # Save to database
    insert_log(str(features), rf_result, int(km_pred))

    return {
        "RandomForest": rf_result,
        "KMeansCluster": int(km_pred)
    }
