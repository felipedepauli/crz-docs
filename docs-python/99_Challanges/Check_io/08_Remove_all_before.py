# In this challange, we have to remove all the items before the first occurrence of the value v.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def removeAllVBefore (lista, v):
    try:
        return lista[lista.index(v):]
    except ValueError:
        return lista

print(removeAllVBefore(lista, 911))