from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.log import Log
from app.schemas.log import LogCreate
from app.routes.auth import get_current_user
from app.services.logs_service import create_log

router = APIRouter(prefix="/logs", tags=["logs"])

def get_db():
    db = SessionLocal()
    try:        
        yield db
    finally:
        db.close()

# @router.post("/upload")
# def upload_log(message: str, level: str, db: Session = Depends(get_db)):
#     new_log = Log(message=message, level=level)
#     db.add(new_log)
#     db.commit()
#     db.refresh(new_log)
    
#     return {"message": "Log uploaded successfully"}

@router.post("/upload")
def upload_log(
    log: LogCreate,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    created_log = create_log(db, log.message, log.level)

    return {
        "id": created_log.id,
        "message": created_log.message,
        "level": created_log.level,
        "anomaly_score": created_log.anomaly_score,
        "is_anomaly": created_log.is_anomaly
    }