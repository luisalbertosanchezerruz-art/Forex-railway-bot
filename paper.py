from app.broker.base import Broker

class PaperBroker(Broker):
    def get_candles(self, symbol, timeframe, limit=200):
        raise NotImplementedError("Connect a market-data provider in V1.1")

    def place_order(self, symbol, side, size, stop, target):
        return {
            "status": "PAPER_FILLED",
            "symbol": symbol,
            "side": side,
            "size": size,
            "stop": stop,
            "target": target,
        }
