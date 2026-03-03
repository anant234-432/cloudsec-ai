from sqlalchemy.orm import Session
from app.models.log import Log
from app.services.anomaly_service import detect_anomaly
from datetime import datetime,timezone


def create_log(db: Session, message: str, level: str):
# Create raw log
    new_log = Log(
        message=message,
        level=level,
        created_at=datetime.now(timezone.utc)
    )

    db.add(new_log)
    db.commit()
    db.refresh(new_log)

# Run anomaly detection
    result = detect_anomaly(message)

# Update log with anomaly results
    new_log.anomaly_score = result["score"]
    new_log.is_anomaly = result["is_anomaly"]

    db.commit()
    db.refresh(new_log)

    return new_log