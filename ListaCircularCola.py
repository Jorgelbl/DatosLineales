#se declara la clase Nodo
class Nodo():
    #metodo constructor de la clase Nodo
    def __init__(self, dato):
        #atributos deL metodo construtor Nodo
        self.dato = dato
        self.siguiente = None

#se declara la clase Lista Circular
class ListaCircularCola():
    #metodo constructor de la clase Lista circular
    def __init__(self):
        #atributos del metodo constructor lista circular
        self.primero = None
        self.ultimo = None

    #metodo para declarar si una cola esta vacia
    def Vacia(self):
        #se retornan valores si la cola esta vacia
        return self.primero == None

    #metodo para agregar elementos al inicio de la cola
    def AgregarElementoInicio(self, dato):
        #comprobamos el metodo con un if-else
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero

    #metodo para agregar elementos al final de la cola
    def AgregarElementoFinal(self, dato):
        # comprobamos el metodo con un if-else
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero

    #metodo para recorrer elementos
    def RecorrerElemento(self):
        aux = self.primero
        contador = 0
        while aux:
            print(aux.dato, end = "-->")
            aux = aux.siguiente
            if aux == self.primero:
                contador += 1
            if contador == 2:
                break

print('Cola Con Lista Circular' '\n')
#instancia la clase
elemento = ListaCircularCola()
#agregamos un elemento al inicio de la cola
elemento.AgregarElementoInicio(1)
#agregamos elementos al final de la cola
elemento.AgregarElementoFinal(2)
elemento.AgregarElementoFinal(3)
#recorremos los elementos de la cola
elemento.RecorrerElemento()