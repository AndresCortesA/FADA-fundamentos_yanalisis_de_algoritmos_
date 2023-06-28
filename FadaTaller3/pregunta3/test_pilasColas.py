import unittest

from pilasColas import PilaConColas


"""
Taller 3 FADA

Andrés Mauricio Arias Cortes
Maher Lopez Rodriguez
Santiago Marin Lozano
"""

class PilaConColasTests(unittest.TestCase):
    def setUp(self):
        self.pila = PilaConColas()

    def test_pushPilaConCola(self):
        self.pila.pushPilaConCola(1)
        self.assertFalse(self.pila.estaVaciaPilaConColas())

    def test_popPilaConColas(self):
        self.assertIsNone(self.pila.popPilaConColas())

        self.pila.pushPilaConCola(1)
        self.pila.pushPilaConCola(2)
        self.assertEqual(self.pila.popPilaConColas(), 2)
        self.assertEqual(self.pila.popPilaConColas(), 1)
        self.assertIsNone(self.pila.popPilaConColas())

    def test_mostrarPilaConColas(self):
        self.assertEqual(self.pila.mostrarPilaConColas(), "La pila está vacía.")

        self.pila.pushPilaConCola(1)
        self.pila.pushPilaConCola(2)
        self.pila.pushPilaConCola(3)
        self.assertEqual(self.pila.mostrarPilaConColas(), "Elementos de la pila:\n3\n2\n1")

if __name__ == '__main__':
    unittest.main()
