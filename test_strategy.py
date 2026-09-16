import pandas as pd
from app.strategy import Strategy

def test_strategy_holds_with_insufficient_data():
    df = pd.DataFrame({"close": [1.0, 1.01]})
    assert Strategy().signal(df) == "HOLD"
