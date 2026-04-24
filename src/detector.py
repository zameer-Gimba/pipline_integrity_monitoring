import numpy as np
from sklearn.ensemble import IsolationForest


# 1. Z-Score Detection
def z_score(series):
    mean = np.mean(series)
    std = np.std(series)
    return (series - mean) / std


def detect_anomalies_zscore(data, threshold=2.5):
    z_scores = z_score(data["pressure"])

    anomalies = np.where(np.abs(z_scores) > threshold)[0]
    return anomalies


# 2. AI Detection (Isolation Forest)
def detect_anomalies_ai(data):
    model = IsolationForest(contamination=0.05, random_state=42)

    X = data[["pressure"]].values
    model.fit(X)

    preds = model.predict(X)

    anomalies = np.where(preds == -1)[0]
    return anomalies


# 3. ENGINEERING THRESHOLD DETECTION 
def detect_anomalies_threshold(data, upper=60, lower=40):
    """
    This aligns directly with your visualization safe zone.
    """
    anomalies = []

    for i, value in enumerate(data["pressure"]):
        if value > upper or value < lower:
            anomalies.append(i)

    return np.array(anomalies)
