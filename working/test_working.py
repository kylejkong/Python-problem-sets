from working import convert
import pytest


def test_convert():

    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8 AM") == "10:00 to 08:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("9:30 AM to 11:30 PM") == "09:30 to 23:30"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_str():
    with pytest.raises(ValueError):
        convert("dog")
    with pytest.raises(ValueError):
        convert("12 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("13 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("5:60 AM - 6:60 PM")
    with pytest.raises(ValueError):
        convert("9:6 AM - 5:0 PM")
    with pytest.raises(ValueError):
        convert(":16 AM - :50 PM")
    with pytest.raises(ValueError):
        convert("12:00 - 13:00")
    with pytest.raises(ValueError):
        convert("12:000 AM to 13:000 PM")
    with pytest.raises(ValueError):
        convert("12:00 MM to 11:00 PM")