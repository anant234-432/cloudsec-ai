from sklearn.ensemble import IsolationForest
import numpy as np

from app.services.feature_service import extract_log_features

rng = np.random.RandomState(42)

model = IsolationForest(
    contamination=0.1,
    random_state=42
)

# training data now has 6 features
X_train = rng.rand(500, 6)

model.fit(X_train)


def detect_anomaly(message: str) -> dict:

    features = extract_log_features(message)

    features = features.reshape(1, -1)

    prediction = model.predict(features)

    score = float(model.decision_function(features)[0])

    return {
        "score": score,
        "is_anomaly": prediction[0] == -1
    }