def rango():
    for i in range(4):
        print(str(i))

def cole1():
    usr = {'Juan':'A','Pedro':'I','Diego':'A','Mengano':'x','Sutano':'A','Perengano':'I'}
    for u,s in usr.copy().items():
        if s != 'A':
            del usr[u]
    print(usr)
        
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


def permutacion():
    a = ["a","b","c"]
    b = ["a","b","c"]
    c = a + b
    return c
## print(permutacion())

def permute(list, s):
   if list == 1:
      return s
   else:
      return [ 
         y + x
         for y in permute(1, s)
         for x in permute(list - 1, s)
      ]
"""print(permute(1, ["a","b","c"]))
print(permute(2, ["a","b","c"]))"""

class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)


