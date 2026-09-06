from etl.clean_normalize import normalize_amount, normalize_phone

def test_normalize_amount():
    assert normalize_amount("You received 5,000 RWF") == 5000.0

def test_normalize_phone():
    assert normalize_phone("250780000000") == "+250780000000"
