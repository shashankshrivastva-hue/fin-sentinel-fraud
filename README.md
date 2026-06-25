# 💳 FinSentinel Fraud Detection

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)

Sub-20ms real-time transactional fraud detection microservice combining real-time feature engineering, Haversine geo-distance, velocity tracking, and anomaly scoring.

---

## 🏛️ Scoring Flow

```mermaid
flowchart TD
    Tx[Incoming Transaction] --> Extractor[Feature Extractor]
    Extractor --> F1[Amount Spike Ratio]
    Extractor --> F2[Haversine Geo-Distance]
    Extractor --> F3[10-Minute Velocity Counter]
    F1 & F2 & F3 --> Scorer[Ensemble Fraud Scorer]
    Scorer --> Decision{Risk Threshold}
    Decision -->|Score >= 0.75| Decline[DECLINE Transaction]
    Decision -->|0.40 <= Score < 0.75| Review[FLAG For Manual Review]
    Decision -->|Score < 0.40| Approve[APPROVE Transaction]
```

## 🛠️ Usage

```bash
pip install -r requirements.txt
pytest tests/ -v
uvicorn src.api.server:app --port 8000
```

## 📜 License
MIT License. Built by [Shashank Shrivastva](https://github.com/shashankshrivastva-hue).
