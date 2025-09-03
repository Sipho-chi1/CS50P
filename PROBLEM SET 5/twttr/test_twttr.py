from twttr import shorten
def test_twttr():
    assert shorten('Hello')=='Hll'
    assert shorten('aeiou')==""
    assert shorten('CS50P')=='CS50P'
    assert shorten('This is CS50P')=='Ths s CS50P'