"""
Taller 3 FADA

Andrés Mauricio Arias Cortes
Maher Lopez Rodriguez
Santiago Marin Lozano
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def combinar(L1, L2):
    # Crear una lista vacía para almacenar la combinación de elementos
    L3 = Nodo(None)
    actual = L3

    # Recorrer ambas listas hasta que se llegue al final de una de ellas
    while L1 is not None and L2 is not None:
        # Comparar los valores actuales de las dos listas
        if L1.valor <= L2.valor:
            # Agregar el valor de L1 a L3
            actual.siguiente = L1
            L1 = L1.siguiente
        else:
            # Agregar el valor de L2 a L3
            actual.siguiente = L2
            L2 = L2.siguiente
        actual = actual.siguiente

    # Agregar los elementos restantes de L1 o L2, en caso de que alguna lista no se haya completado
    if L1 is not None:
        actual.siguiente = L1
    if L2 is not None:
        actual.siguiente = L2

    # Retornar la lista combinada sin el nodo inicial vacío
    return L3.siguiente
