import pandas as pd
from app.config import settings

class Strategy:
    def __init__(self):
        self.ema_fast = 20
        self.ema_slow = 50
        self.rsi_period = 14

    def info(self):
        return {
            "name": "EMA20/EMA50 + RSI + ATR",
            "timeframe": settings.timeframe,
            "entry": "trend + momentum confirmation",
            "stop": f"{settings.atr_stop_multiplier} x ATR",
            "target": f"{settings.risk_reward}R",
        }

    def signal(self, df: pd.DataFrame):
        if len(df) < max(self.ema_slow, self.rsi_period) + 5:
            return "HOLD"

        d = df.copy()
        d["ema20"] = d["close"].ewm(span=self.ema_fast, adjust=False).mean()
        d["ema50"] = d["close"].ewm(span=self.ema_slow, adjust=False).mean()

        delta = d["close"].diff()
        gain = delta.clip(lower=0).rolling(self.rsi_period).mean()
        loss = (-delta.clip(upper=0)).rolling(self.rsi_period).mean()
        rs = gain / loss.replace(0, float("nan"))
        d["rsi"] = 100 - (100 / (1 + rs))

        last = d.iloc[-1]
        if last.ema20 > last.ema50 and 50 < last.rsi < 70:
            return "BUY"
        if last.ema20 < last.ema50 and 30 < last.rsi < 50:
            return "SELL"
        return "HOLD"
