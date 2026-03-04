from sklearn.ensemble import IsolationForest
import numpy as np

rng = np.random.RandomState(42)
model = IsolationForest(contamination=0.1, random_state=42)

# Dummy training data (lengths)
X_train = rng.randint(1, 200, size=(300, 1))
model.fit(X_train)

def detect_anomaly(message: str) -> dict:
    value = len(message)  # simple feature for now

    prediction = model.predict([[value]])
    score = float(model.decision_function([[value]])[0])

    return {
        "score": score,
        "is_anomaly": prediction[0] == -1
    }