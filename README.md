# Forex Railway Bot V1

Paper-trading Forex bot designed for Railway.

## V1 scope
- EURUSD, GBPUSD, USDJPY
- H1 strategy
- EMA 20/50 trend filter
- RSI momentum filter
- ATR-based stop loss
- Risk-based position sizing (default 0.5%)
- Paper broker
- SQLite by default; PostgreSQL-ready via DATABASE_URL
- FastAPI health/status endpoints
- Docker/Railway deployment ready

## Run locally
```bash
cp .env.example .env
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://localhost:8000/health

## Important
This version does NOT place real orders. Broker integration is intentionally isolated in `app/broker/`.
