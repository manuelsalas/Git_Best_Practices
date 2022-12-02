# Implementación de lista enlazada simple
from ast import Return
from asyncio.windows_events import NULL
from sre_compile import isstring

class Nodo:
    def __init__(self, dato):
      self.dato = dato
      self.next = NULL

class Lista:
    def __init__(self):
      self.header = NULL

    def agregar_nodo(self, dato):
      # Agrega siempre al final de la lista
      if isstring(dato) == False:
        print("agregar_nodo: dato no es string")
        return -1
      if self.header == NULL:
       self.header = Nodo(dato)
       return 0
      aux = self.header
      while aux.next != NULL:
        aux = aux.next
      aux.next = Nodo(dato)
      return 0

    def recorrer_lista(self):
      if self.header == NULL:
        print("Lista vacia")
        return 0
      else:
        nodo = self.header
      while nodo.next != NULL:
        print("Dato:"+nodo.dato)
        nodo = nodo.next
      else:
        print("Dato:"+nodo.dato)

    def buscar_clave(self,clave):
      if self.header == NULL:
        print("Lista vacia")
        return 0
      else:
        nodo = self.header
      while nodo.next != NULL:
          if nodo.dato == clave:
            print("Clave : "+nodo.dato)
            return nodo
          nodo = nodo.next
      else:
        if nodo.dato == clave:
          print("Clave : "+nodo.dato)
          return nodo
        else:
          print("Clave no existe en la lista")
          return -1

    def largo_lista(self):
      if self.header == NULL:
        print("Lista vacia")
        return 0
      else:
        nodo = self.header
      i = 1
      while nodo.next != NULL:
        i = i + 1
        nodo = nodo.next
      print("Nodos en la lista : "+str(i))
      return i

    def borrar_por_clave(self,clave):
      if self.header == NULL:
        print("Lista vacia")
        return 0
      else:
        nodo = self.header
        nant = NULL
      existe = False
      while nodo.next != NULL:
          if nodo.dato == clave:
            existe = True
            break
          nant = nodo
          nodo = nodo.next
      else:
        if nodo.dato == clave:
          existe = True

      if existe == True:
        nant.next = nodo.next
        print("Clave Borrada : "+nodo.dato)
        return 0
      else:
        print("Clave no existe en la lista")
        return -1
    
a = Lista()
a.agregar_nodo("Hola Mundo")
a.agregar_nodo("Chao Mundo")
a.agregar_nodo("Borrar")
a.agregar_nodo("Manuel")
a.agregar_nodo("Ignacio")
a.recorrer_lista()
a.buscar_clave("Borrar")
a.largo_lista()
a.borrar_por_clave("Borrar")
a.recorrer_lista()
a.buscar_clave("Borrar")
a.largo_lista()
