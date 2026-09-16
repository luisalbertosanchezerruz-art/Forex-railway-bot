from fastapi import FastAPI
from app.config import settings
from app.strategy import Strategy
from app.risk import RiskManager

app = FastAPI(title="Forex Railway Bot V1", version="1.0.0")

strategy = Strategy()
risk = RiskManager()

@app.get("/health")
def health():
    return {"status": "ok", "environment": settings.app_env, "mode": "paper"}

@app.get("/status")
def status():
    return {
        "symbols": settings.symbols_list,
        "timeframe": settings.timeframe,
        "risk_per_trade": settings.risk_per_trade,
        "max_open_positions": settings.max_open_positions,
    }

@app.get("/strategy")
def strategy_info():
    return strategy.info()
