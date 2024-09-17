# archivo: test_calculadora.py

import unittest
from ModuloAProbar import sumar, restar  # Importamos las funciones que vamos a probar


class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)  # Esperamos que sumar(2, 3) devuelva 5
        self.assertEqual(sumar(-1, 1), 0)  # Suma de números positivos y negativos
        self.assertEqual(sumar(0, 0), 0)  # Suma de ceros

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)  # Esperamos que restar(5, 3) devuelva 2
        self.assertEqual(restar(0, 0), 0)  # Resta de ceros
        self.assertEqual(restar(10, 5), 5)  # Resta de números positivos


# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
