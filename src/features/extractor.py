"""Real-time transaction feature engineering."""
import math
from typing import Dict, Any

class FeatureExtractor:
    @staticmethod
    def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Calculates distance between two geographic coordinates in kilometers."""
        r = 6371.0 # Earth radius in km
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return r * c

    @staticmethod
    def extract_features(tx: Dict[str, Any], user_profile: Dict[str, Any]) -> list[float]:
        # Amount deviation
        avg_amt = user_profile.get("avg_amount", 50.0)
        amt_ratio = tx["amount"] / max(1.0, avg_amt)

        # Distance from usual home location
        dist_km = FeatureExtractor.haversine_distance(
            tx.get("lat", 0.0), tx.get("lon", 0.0),
            user_profile.get("home_lat", 0.0), user_profile.get("home_lon", 0.0)
        )

        # Velocity check (txs in last 10 mins)
        velocity = tx.get("velocity_10m", 1)

        return [amt_ratio, dist_km, float(velocity)]
