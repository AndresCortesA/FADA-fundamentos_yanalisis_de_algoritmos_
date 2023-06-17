class Obra:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class Nodo:
    def __init__(self, obra, siguiente=None):
        self.obra = obra
        self.siguiente = siguiente

class Inventario:
    def __init__(self):
        self.cabeza = None

    def agregarReplica(self, nombre):
        if self.cabeza is None:
            self.cabeza = Nodo(Obra(nombre, 1))
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                if nodo_actual.obra.nombre == nombre:
                    nodo_actual.obra.cantidad += 1
                    return
                nodo_actual = nodo_actual.siguiente

            if nodo_actual.obra.nombre == nombre:
                nodo_actual.obra.cantidad += 1
            else:
                nodo_actual.siguiente = Nodo(Obra(nombre, 1))

    def venderReplica(self, nombre):
        if self.cabeza is None:
            print("No hay obras disponibles con el nombre especificado.")
            return

        if self.cabeza.obra.nombre == nombre:
            if self.cabeza.obra.cantidad > 1:
                self.cabeza.obra.cantidad -= 1
            else:
                self.cabeza = self.cabeza.siguiente
            return

        nodo_actual = self.cabeza
        while nodo_actual is not None and nodo_actual.siguiente is not None:
            if nodo_actual.siguiente.obra.nombre == nombre:
                if nodo_actual.siguiente.obra.cantidad > 1:
                    nodo_actual.siguiente.obra.cantidad -= 1
                else:
                    nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return
            nodo_actual = nodo_actual.siguiente

        print("No hay obras disponibles con el nombre especificado.")




    def listarReplicas(self):
        if self.cabeza is None:
            print("No hay obras en el inventario.")
            return

        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print("Obra:", nodo_actual.obra.nombre)
            print("Cantidad disponible:", nodo_actual.obra.cantidad)
            print("----------------------------")
            nodo_actual = nodo_actual.siguiente
