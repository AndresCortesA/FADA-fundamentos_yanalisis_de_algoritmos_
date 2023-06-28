from queue import Queue

class PilaConColas:
    def __init__(self):
        self.cola = Queue()

    def estaVaciaPilaConColas(self):
        return self.cola.empty()

    def pushPilaConCola(self, elemento):
        self.cola.put(elemento)

    def popPilaConColas(self):
        if self.estaVaciaPilaConColas():
            return None

        # Mover los elementos de la cola a una nueva cola
        nueva_cola = Queue()
        while self.cola.qsize() > 1:
            nueva_cola.put(self.cola.get())

        # Extraer el elemento en la parte superior de la pila
        elemento = self.cola.get()

        # Reemplazar la cola original por la nueva cola
        self.cola = nueva_cola

        return elemento

    def mostrarPilaConColas(self):
        if self.estaVaciaPilaConColas():
            return "La pila está vacía."

        elementos = []
        while not self.cola.empty():
            elementos.append(self.cola.get())
        
        pila_string = "Elementos de la pila:\n"
        pila_string += "\n".join(str(elem) for elem in elementos[::-1])

        return pila_string


pila = PilaConColas()

print(pila.estaVaciaPilaConColas())  # True

pila.pushPilaConCola("Elemento 1")
pila.pushPilaConCola("Elemento 2")

print(pila.estaVaciaPilaConColas())  # False

print(pila.popPilaConColas())  # "Elemento 2"
print(pila.popPilaConColas())  # "Elemento 1"
print(pila.popPilaConColas())  # None

pila.mostrarPilaConColas()
# La pila está vacía.
