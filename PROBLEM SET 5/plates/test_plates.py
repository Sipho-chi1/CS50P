from plates import is_valid
def test_len():
    assert is_valid('CS')==True
    assert is_valid('HEF')==True
    assert is_valid('HELLOTHERE')==False
    assert is_valid('H')==False
    assert is_valid('')==False

def test_char():
    assert is_valid('CS50')==True
    assert is_valid('CS50P')==False
    assert is_valid('CS@50')==False
    assert is_valid('CS 50')==False
    assert is_valid('CS-50')==False

def test_num():
    assert is_valid('CS50')==True
    assert is_valid('CS05')==False
    assert is_valid('CS5')==True
    assert is_valid('CS500')==True
    assert is_valid('CS5000')==True
    assert is_valid('CS50P')==False
    assert is_valid('CS50P1')==False

def test_start():
    assert is_valid('50CS')==False
    assert is_valid('C50S')==False
    assert is_valid('CS50')==True
    assert is_valid('C')==False
    assert is_valid('5')==False


