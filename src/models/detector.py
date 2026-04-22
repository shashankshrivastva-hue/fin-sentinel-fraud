"""Inference scoring engine combining rule heuristics and ML anomaly score."""
from typing import Dict, Any
from ..features.extractor import FeatureExtractor

class FraudDetector:
    def __init__(self, high_risk_threshold: float = 0.75):
        self.threshold = high_risk_threshold

    def score_transaction(self, tx: Dict[str, Any], profile: Dict[str, Any]) -> Dict[str, Any]:
        features = FeatureExtractor.extract_features(tx, profile)
        amt_ratio, dist_km, velocity = features

        score = 0.0
        reasons = []

        # Heuristic rules + anomaly weighting
        if amt_ratio > 4.0:
            score += 0.45
            reasons.append("Extreme transaction amount spike")

        if dist_km > 1000.0:
            score += 0.35
            reasons.append("Geographic anomaly: location far from user baseline")

        if velocity >= 5:
            score += 0.30
            reasons.append("Rapid transaction velocity burst")

        score = min(1.0, score)
        decision = "DECLINE" if score >= self.threshold else ("REVIEW" if score >= 0.40 else "APPROVE")

        return {
            "transaction_id": tx.get("id"),
            "fraud_score": round(score, 3),
            "decision": decision,
            "reasons": reasons,
            "features": {
                "amount_ratio": round(amt_ratio, 2),
                "distance_km": round(dist_km, 2),
                "velocity": velocity
            }
        }
