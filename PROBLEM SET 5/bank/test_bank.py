from bank import value
def test_helo():
    assert value('Hello')=='$0'
    assert value('hello')=='$0'
    assert value('John, hello')=='$0'
    assert value('HELLO')=='$0'
def est_h():
    assert value('Hi')=='$20'
    assert value('howdy')=='$20'
    assert value('H')=='$20'
    assert value('h')=='$20'
    assert value('hoi,hoi')=='$20'

def test_other():
    assert value('John')=='$100'
    assert value('Alice')=='$100'
    assert value('Zebra')=='$100'
    assert value('CS50P')=='$100'
    assert value('Python')=='$100'