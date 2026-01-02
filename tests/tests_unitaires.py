import unittest
from src.polynom import Polynome

class TestPolynomeMethods(unittest.TestCase):

    def test_Constructeur(self):
        self.assertEqual(Polynome(), [])
        self.assertEqual(Polynome(1), [1])
        self.assertEqual(Polynome((1,2,3)), [1,2,3])
    
    def test_mul(self):
        a = Polynome((1, 2, 3))
        self.assertEqual(a*10,[10,20,30])
if __name__ == '__main__':
    unittest.main()