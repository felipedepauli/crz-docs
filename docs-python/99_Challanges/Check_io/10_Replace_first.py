# Vamos fazer do jeito mais porco
list = [1, 2, 3, 5, 6, 7, 8, 9, 10]

# Solution 01
def replace_first_1(list):
    temp = list[0]
    list[0] = list[-1]
    list[-1] = temp
    return list

print(replace_first_1(list))
# Solution 02
def replace_first_2(list):
    list[0], list[-1] = list[-1], list[0]
    return list



print(replace_first_2(list))
print(replace_first_2(list))

# Agora vamos fazer de um jeito novo. O primeiro vai para o fim da fila
# e todos os outros vão para frente.

def replace_first_3(list):
    list.append(list.pop(0))
    return list

print(list)
print(replace_first_3(list))

def replace_first_4(items: list) -> list:
    return items[1:] + items[:1]

print(list)
print(replace_first_4(list))