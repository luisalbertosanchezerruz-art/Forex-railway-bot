from app.risk import RiskManager

def test_position_size():
    size = RiskManager().position_size(10000, 10)
    assert size == 5
