from etl.categorize import categorize

def test_incoming_money():
    assert categorize("You have received 5,000 RWF from John") == "incoming_money"


def test_payment():
    assert categorize("Payment of 1,000 RWF to Shop") == "payment"


def test_other():
    assert categorize("Your OTP is 123456") == "other"
