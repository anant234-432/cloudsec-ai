from fastapi import APIRouter, Depends
from app.services.anomaly_service import detect_anomaly
from app.schemas.ai import AIRequest
from app.routes.auth import get_current_user

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/analyze")
def analyze(request: AIRequest, current_user: str = Depends(get_current_user)):
    
    result = detect_anomaly(request.value)
    return {
        "anomaly": bool(result),
        "score": result,
        "analyzed_by": current_user
    }