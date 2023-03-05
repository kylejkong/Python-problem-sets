from twttr import shorten



def test_twttr():

    assert shorten("hello") == "hll"
    assert shorten("Hello") == "Hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("hELLO") == "hLL"
    assert shorten("hello, world") == "hll, wrld"
    assert shorten("69") == "69"
    assert shorten("cs50") == "cs50"
    assert shorten("!?/") == "!?/"
    assert shorten("hello, 420") == "hll, 420"
