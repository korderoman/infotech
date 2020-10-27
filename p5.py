import math
def suma(list:list)->int:
    suma=sum(list)
    return suma

def producto(list:list)->int:
    producto=math.prod(list)
    return producto


print(suma([1,3,5]))
print(producto([1,5,6]))