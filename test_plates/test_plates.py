from plates import is_valid


def test_plates_length():
    assert is_valid("zambia") == True
    assert is_valid("america") == False
    assert is_valid("a") == False


def test_plates_number():
    assert is_valid("cs50") == True
    assert is_valid("cs5s0") == False
    assert is_valid("50cs") == False
    assert is_valid("c50") == False
    assert is_valid("50") == False
    assert is_valid("") == False
    assert is_valid("0") == False
    assert is_valid(" ")==False
    assert is_valid("cs50?!") == False
    assert is_valid("cs05") == False









