import unittest
import trader as trad
#This needs to be completely overhauled at a later period

class TestGetQuote(unittest.TestCase):

    def test_type_get_quote():
        word = trad.generator.get_quote("AAPL")
        self.assertEqual(type(word), float64)
        self.assertFalse(type(word), str)
        
    '''
    sdef test_get_quote():
        l = ('AAPL')    
        word = trad.generator.get_quote("AAPL")
        assert l in word
    '''

if __name__ == '__main__':
    unittest.main()

