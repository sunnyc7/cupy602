import unittest
from trader import generator

#This needs to be completely overhauled at a later period

def test_type_get_quote():
    word = generator.get_quote("AAPL")        
    assert 'AAPL' in word
    #assert 'float64' in word
    assert type(word) != str
        
    '''
    def test_get_quote():
        l = ('AAPL')    
        word = trad.generator.get_quote("AAPL")
        assert l in word
    '''