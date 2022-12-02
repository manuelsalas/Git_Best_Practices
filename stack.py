import string


class Nodo:
    def __init__(self, dato:string):
      self.dato = dato
      self.next = None
class Stack:
    def __init__(self):
      self.tope = None
    def push(self, dato):
        if self.tope == None:
            self.tope = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.next = self.tope
            self.tope = aux
    def pop(self):
        if self.tope == None:
            return None
        else:
            aux = self.tope
            self.tope = aux.next
            return aux.dato
    def lista_stack(self):
        assert self.tope is not None
        i = 1
        aux = self.tope
        while aux.next != None:
            print(str(i)+" : "+str(aux.dato))
            i = i + 1
            aux = aux.next
        print(str(i)+" : "+str(aux.dato))
        
            
s = Stack()
s.push("Uno")
s.push("Dos")
s.push("Tres")
s.push("Cuatro")
s.lista_stack()
print("Pop() = "+str(s.pop()))
s.lista_stack()

