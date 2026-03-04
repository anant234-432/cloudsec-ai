from typing import Optional

from pydantic import BaseModel

class LogCreate(BaseModel):
    message: str
    level: str

class LogResponse(BaseModel):
    id: int
    message: str
    level: str
    created_at: str
    anomaly_score: Optional[float] = None
    is_anomaly: int
    explanation: Optional[str] = None

    class Config:
        from_attributes = True