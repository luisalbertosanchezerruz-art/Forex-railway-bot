from app.broker.base import Broker

class XTBClient(Broker):
    """Placeholder for XTB xAPI integration. No live trading in V1."""
    def __init__(self, *args, **kwargs):
        self.enabled = False

    def get_candles(self, symbol, timeframe, limit=200):
        raise NotImplementedError("XTB xAPI integration is planned for the next phase")

    def place_order(self, symbol, side, size, stop, target):
        raise RuntimeError("Live execution disabled in V1")
