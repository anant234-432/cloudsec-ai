from fastapi import APIRouter, Depends
from app.services.anomaly_service import detect_anomaly
from app.schemas.ai import AIRequest
from app.routes.auth import get_current_user
from app.services.ai_service import score_log_message

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/analyze")
def analyze(request: AIRequest, current_user: str = Depends(get_current_user)):
    scored = score_log_message(request.message)
    return {
        "anomaly": bool(scored["is_anomaly"]),
        "score": scored["anomaly_score"],
        "explanation": scored["explanation"],
        "analyzed_by": current_user
    }