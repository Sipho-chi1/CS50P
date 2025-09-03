from refueling import convert, gauge
import pytest
def test_convert():
    assert convert('1/2')==50 and gauge(50)=='50%'
    assert convert('3/4')==75 and gauge(75)=='75%'
    assert convert('4/4')==100 and gauge(100)=='F'
    assert convert('1/4')==25 and gauge(25)=='25%'
    assert convert('2/4')==50 and gauge(50)=='50%'

def test_zero():
    assert convert('0/1')==0 and gauge(0)=='E'
    assert convert('0/4')==0 and gauge(0)=='E'
    assert convert('0/5')==0 and gauge(0)=='E'

def test_error():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('a/b')
    with pytest.raises(ValueError):
        convert('1/a')
    with pytest.raises(ValueError):
        convert('a/1')
    