"""FastAPI sub-20ms fraud scoring endpoint."""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from ..models.detector import FraudDetector

app = FastAPI(title="FinSentinel Fraud API", version="1.0.0")
detector = FraudDetector()

class TransactionRequest(BaseModel):
    id: str
    user_id: str
    amount: float
    lat: float
    lon: float
    velocity_10m: Optional[int] = 1

@app.post("/api/v1/score")
def score(tx: TransactionRequest):
    # Mock user profile
    profile = {"avg_amount": 45.0, "home_lat": 40.7128, "home_lon": -74.0060}
    result = detector.score_transaction(tx.model_dump(), profile)
    return result
