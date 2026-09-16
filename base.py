from abc import ABC, abstractmethod

class Broker(ABC):
    @abstractmethod
    def get_candles(self, symbol: str, timeframe: str, limit: int = 200):
        ...

    @abstractmethod
    def place_order(self, symbol: str, side: str, size: float, stop: float, target: float):
        ...
