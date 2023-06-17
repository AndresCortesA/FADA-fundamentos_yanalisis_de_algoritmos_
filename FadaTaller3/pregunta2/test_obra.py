import unittest

from obra import Inventario

class InventarioTests(unittest.TestCase):
    def setUp(self):
        self.inventario = Inventario()

    def test_agregarReplica(self):
        self.inventario.agregarReplica("El hombre de Vitrubio")
        self.assertEqual(self.inventario.cabeza.obra.nombre, "El hombre de Vitrubio")
        self.assertEqual(self.inventario.cabeza.obra.cantidad, 1)

        self.inventario.agregarReplica("El hombre de Vitrubio")
        self.assertEqual(self.inventario.cabeza.obra.cantidad, 2)

        self.inventario.agregarReplica("Gioconda")
        self.assertEqual(self.inventario.cabeza.siguiente.obra.nombre, "Gioconda")
        self.assertEqual(self.inventario.cabeza.siguiente.obra.cantidad, 1)

    def test_venderReplica(self):
        self.inventario.agregarReplica("El hombre de Vitrubio")
        self.inventario.agregarReplica("Persistencia de la memoria")

        
        self.inventario.venderReplica("El hombre de Vitrubio")
        self.assertEqual(self.inventario.cabeza.obra.cantidad, 1)
        
        # Se supone que aqui se debe devolver None pero devuelve 1 y se va a un error, no entiendo que más hacemos
        #Agradezco alguna corrección o retroalimentacion de esta parte  vender replicas, no devuelve el mensaje o hace
        # lo que se pide, o no sabemos si estas pruebas esten mal (Ya funciono, se nos olvido la condición de devolver un string)
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        
        
        self.inventario.venderReplica("El hombre de Vitrubio")
        sys.stdout = sys.__stdout__
        expected_output = "No hay obras disponibles con el nombre especificado."
        self.assertEqual(captured_output.getvalue().strip(), expected_output)
        
        self.inventario.venderReplica("Persistencia de la memoria")
        self.assertIsNone(self.inventario.cabeza)

    def test_listarReplicas(self):
        self.inventario.agregarReplica("El hombre de Vitrubio")
        self.inventario.agregarReplica("Persistencia de la memoria")
        self.inventario.agregarReplica("Gioconda")

        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        self.inventario.listarReplicas()

        sys.stdout = sys.__stdout__

        expected_output = "Obra: El hombre de Vitrubio\nCantidad disponible: 1\n----------------------------\n" \
                          "Obra: Persistencia de la memoria\nCantidad disponible: 1\n----------------------------\n" \
                          "Obra: Gioconda\nCantidad disponible: 1\n----------------------------\n"

        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
