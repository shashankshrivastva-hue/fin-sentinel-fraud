from src.models.detector import FraudDetector

def test_fraud_decline_on_extreme_anomaly():
    detector = FraudDetector()
    tx = {"id": "tx-1", "amount": 1000.0, "lat": 10.0, "lon": 20.0, "velocity_10m": 8}
    profile = {"avg_amount": 25.0, "home_lat": 40.71, "home_lon": -74.00}
    res = detector.score_transaction(tx, profile)
    assert res["decision"] == "DECLINE"
    assert res["fraud_score"] >= 0.75
