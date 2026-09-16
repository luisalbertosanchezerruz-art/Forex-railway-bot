from app.config import settings

class RiskManager:
    def position_size(self, equity: float, stop_distance: float, value_per_unit: float = 1.0):
        if equity <= 0 or stop_distance <= 0 or value_per_unit <= 0:
            return 0.0
        risk_amount = equity * settings.risk_per_trade
        return risk_amount / (stop_distance * value_per_unit)

    def can_trade(self, daily_pnl: float, open_positions: int) -> bool:
        if open_positions >= settings.max_open_positions:
            return False
        if daily_pnl <= -(settings.max_daily_loss):
            return False
        return True
