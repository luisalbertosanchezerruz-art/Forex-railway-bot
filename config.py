from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_env: str = "paper"
    database_url: str = "sqlite:///./data/trading.db"
    symbols: str = "EURUSD,GBPUSD,USDJPY"
    timeframe: str = "H1"
    risk_per_trade: float = 0.005
    max_open_positions: int = 3
    max_daily_loss: float = 0.02
    atr_period: int = 14
    atr_stop_multiplier: float = 1.5
    risk_reward: float = 2.0
    poll_seconds: int = 60

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def symbols_list(self):
        return [x.strip() for x in self.symbols.split(",") if x.strip()]

settings = Settings()
