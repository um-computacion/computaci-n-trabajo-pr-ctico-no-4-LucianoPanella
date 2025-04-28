import unittest
from src.factorial import factorial_iterative, factorial_recursive
class TestFactorial(unittest.TestCase):
    #Agrego test para la funcion factorial iterativa

    #Test de factorial zero 
    def test_factorial_iterative_zero(self):
        self.assertEqual(factorial_iterative(0), 1)
    
    #Test de factorial 
    def test_factorial_iterative(self):
        
        self.assertEqual(factorial_iterative(1), 1)
        self.assertEqual(factorial_iterative(3), 6)
        self.assertEqual(factorial_iterative(4), 24)
        self.assertEqual(factorial_iterative(10), 3628800)

    #Test de factorial negativo
    def test_factorial_iterative_negative(self):
        with self.assertRaises(ValueError):
            factorial_iterative(-1)
    
    #Agrego test para la funcion factorial recursiva

    #Test de factorial zero
    def test_factorial_recursive_zero(self):
        self.assertEqual(factorial_recursive(0), 1)

    #Test de factorial
    def test_factorial_recursive(self):
        self.assertEqual(factorial_recursive(1), 1)
        self.assertEqual(factorial_recursive(3), 6)
        self.assertEqual(factorial_recursive(4), 24)
        self.assertEqual(factorial_recursive(10), 3628800)

    #Test de factorial negativo
    def test_factorial_recursiva_negative(self):
        with self.assertRaises(ValueError):
            factorial_recursive(-1)

if __name__ == '__main__':
    unittest.main()