from app.services.anomaly_service import detect_anomaly

def score_log_message(message: str) -> dict:
    """
    Returns:
      {
        "anomaly_score": float,
        "is_anomaly": int,   # 0/1
        "explanation": str | None
      }
    """
    result = detect_anomaly(message)

    anomaly_score = result["score"]
    is_anomaly = 1 if result["is_anomaly"] else 0

    # Simple placeholder explanation (can be upgraded to LLM)
    explanation = None
    if is_anomaly:
        explanation = "Detected as anomalous based on current feature extraction."

    return {
        "anomaly_score": anomaly_score,
        "is_anomaly": is_anomaly,
        "explanation": explanation,
    }