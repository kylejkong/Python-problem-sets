from numb3rs import validate

def main():
    test1()
    test2()



def test1():
    assert validate(r'1.2.3.4') == True
    assert validate(r'2.3.4') == False
    assert validate(r'3.4') == False
    assert validate(r'4') == False
    assert validate(r'1.2.3.4.') == False
    assert validate(r'.1.2.3.4.') == False



def test2():

    assert validate(r'256.256.256.256') == False
    assert validate(r'255.254.253.252') == True
    assert validate(r'255.255.255.999') == False
    assert validate(r'1.2.3.1000') == False


if __name__ == "__main__":
    main()
