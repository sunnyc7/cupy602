import unittest

from trader import generator
#This needs to be completely overhauled at a later period

def test_get_quote():
    l = ('AAPL')
    word = trader.get_quote("AAPL")
    assert l in word

 def test_type_get_quote():
    word = trader.get_quote("AAPL")
    assert type(word) == float64
    assert nottype(word) == str    

'''
def test_sample_multiple_word():
    l = ('foo','bar','foobar')
    words = generator.sample(l,2)
    assert len(words) == 2
    assert words[0] in l
    assert words[1] in l
    assert words[0] is not words[1]

def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >=5
    
'''

