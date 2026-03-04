from time import timezone

from sqlalchemy import Column, DateTime, Integer, String, Float
from app.database import Base
from datetime import datetime, timezone

class Log(Base):
    __tablename__= "logs"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    level = Column(String)
    created_at = Column(DateTime, default = lambda: datetime.now(timezone.utc))
    anomaly_score = Column(Float, nullable=True)
    is_anomaly = Column(Integer, default=0)  # 0 for normal, 1 for anomaly
    explanation = Column(String, nullable=True)