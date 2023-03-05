from bank import value


def test_bank_0():

    assert value("hello") == 0
    assert value("HELLO") == 0


def test_bank_20():

    assert value("HI") == 20
    assert value("hi") == 20


def test_bank_100():

    assert value("seinfeld") == 100
    assert value("Seinfeld") == 100