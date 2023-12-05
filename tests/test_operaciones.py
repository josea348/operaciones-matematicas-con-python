import unittest
from mi_libreria.operaciones import sumar, restar, multiplicar, dividir

class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 4), 8)

    def test_dividir(self):
        self.assertEqual(dividir(8, 2), 4)
        with self.assertRaises(ValueError):
            dividir(5, 0)

if __name__ == '__main__':
    unittest.main()
