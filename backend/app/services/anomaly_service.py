from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest(contamination=0.1)

# Dummy training data
X_train = np.random.rand(100, 1)
model.fit(X_train)

def detect_anomaly(message: str):
    value = len(message)  # simple feature for now

    prediction = model.predict([[value]])
    score = float(model.decision_function([[value]])[0])

    return {
        "score": score,
        "is_anomaly": prediction[0] == -1
    }