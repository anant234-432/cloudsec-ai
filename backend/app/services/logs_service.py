from sqlalchemy.orm import Session
from app.models.log import Log
from app.services.ai_service import score_log_message


def create_log(db: Session, message: str, level: str)-> Log:
    scored = score_log_message(message)

    new_log = Log(
        message=message,
        level=level,
        anomaly_score=scored["anomaly_score"],
        is_anomaly=scored["is_anomaly"],
        explanation=scored["explanation"],
    )

    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log