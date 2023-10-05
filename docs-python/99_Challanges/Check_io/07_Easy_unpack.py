lista = (1, 3, 4, 2, 6, 7, 8, 9, 5)

# Solution 1
def unpack_1(lista):
    return (lista[0], lista[2], lista[-2])

print(unpack_1(lista))


# Solution 02
unpack_2 = lambda elements : (elements[0], elements[2], elements[-2])
print(unpack_2(lista))

# Solution 03
from operator import itemgetter
unpack_3 = itemgetter(0, 2, ~1)

print(unpack_3(lista))

# Solution 04
import numpy as np
def unpack_4(lista):
    lista_array = np.array(lista)
    return tuple(lista_array[[0, 2, -2]])

print(unpack_4(lista))