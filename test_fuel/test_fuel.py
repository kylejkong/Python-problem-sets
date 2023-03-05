from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("0/4") == 0


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"


def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")



