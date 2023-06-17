import unittest

from combinar import Nodo, combinar

"""
Taller 3 FADA

Andrés Mauricio Arias Cortes
Maher Lopez Rodriguez
Santiago Marin Lozano
"""

class CombinarTestCase(unittest.TestCase):
    def test_combinar(self):
        # Crea las listas de ejemplo
        L1 = Nodo(3)
        L1.siguiente = Nodo(7)
        L1.siguiente.siguiente = Nodo(9)

        L2 = Nodo(1)
        L2.siguiente = Nodo(3)
        L2.siguiente.siguiente = Nodo(8)
        
        print("Lista 1:", L1)
        print("Lista 2:", L2)

        # Llamamos a la función combinar
        L3 = combinar(L1, L2)

        # Verificamos el resultado esperado
        resultado = []
        actual = L3
        while actual is not None:
            resultado.append(actual.valor)
            actual = actual.siguiente

        self.assertEqual(resultado, [1, 3, 3, 7, 8, 9])

