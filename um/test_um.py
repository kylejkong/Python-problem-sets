from um import count


def test_count():

    assert count("um") == 1
    assert count("album") == 0
    assert count("um, album") == 1
    assert count("um....  umalum") == 1
    assert count("um... what are regular expressions?") == 1
    assert count("um, thanks, um, regular expressions make sense now.") == 2
    assert count('um? Mum? Is this that album where, um, umm, the clumsy alums play drums?') == 2
    assert count('UM') == 1