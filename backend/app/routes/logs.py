from typing import Optional
from fastapi import APIRouter, Depends, Query, HTTPException
from httpx import get
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.log import Log
from app.schemas.log import LogCreate
from app.routes.auth import get_current_user
from app.services.logs_service import create_log
from app.database import SessionLocal
from typing import Optional

router = APIRouter(prefix="/logs", tags=["logs"])

def get_db():
    db = SessionLocal()
    try:        
        yield db
    finally:
        db.close()

@router.post("/upload")
def upload_log(
    log: LogCreate,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)   
):
    created = create_log(db, log.message, log.level)
    return {
        "id": created.id,
        "message": created.message,
        "level": created.level,
        "created_at": created.created_at,
        "anomaly_score": created.anomaly_score,
        "is_anomaly": created.is_anomaly,
        "explanation": created.explanation,
    }


@router.get("")
def list_logs(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    level: Optional[str] = Query(None, ge=0, le=1),
    is_anomaly: Optional[int] = Query(None, ge=0, le=1)
):
    q=db.query(Log)
    if level:
        q = q.filter(Log.level == level)
    if is_anomaly is not None:
        q = q.filter(Log.is_anomaly == is_anomaly)

    logs=q.order_by(Log.created_at.desc()).offset(offset).limit(limit).all()

    return [
        {
            "id": log.id,
            "message": log.message,
            "level": log.level,
            "created_at": log.created_at,
            "anomaly_score": log.anomaly_score,
            "is_anomaly": log.is_anomaly,
            "explanation": log.explanation,
        }
        for log in logs
    ]

@router.get("/anomalies")
def list_anomalies(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    logs = (
        db.query(Log)
        .filter(Log.is_anomaly == 1)
        .order_by(Log.created_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
    return [
        {
            "id": log.id,
            "message": log.message,
            "level": log.level,
            "created_at": str(log.created_at),
            "anomaly_score": log.anomaly_score,
            "is_anomaly": log.is_anomaly,
            "explanation": log.explanation
        }
        for log in logs
    ]


@router.get("/{log_id}")
def get_log(
    log_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    log = db.query(Log).filter(Log.id == log_id).first()
    if not log:
        raise HTTPException(status_code=404, detail="Log not found")

    return {
        "id": log.id,
        "message": log.message,
        "level": log.level,
        "created_at": str(log.created_at),
        "anomaly_score": log.anomaly_score,
        "is_anomaly": log.is_anomaly,
        "explanation": log.explanation
    }

