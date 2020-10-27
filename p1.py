import random
"""
Se asume que los número ya están dados y aleatorios
"""
ordenados=sorted([ round(random.random()*(100+x))   for x in range(0,10)])
print(ordenados)