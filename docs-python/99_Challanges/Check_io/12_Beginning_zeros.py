# You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

# Input: A string, that consist of digits.
# Output: An Int. 

# Solution 01

def beginning_zeros(sequence):
    count = 0
    for i in sequence:
        if i == '0':
            count += 1
        else:
            break;
    return count

assert beginning_zeros('100') == 0
assert beginning_zeros('001') == 2
assert beginning_zeros('100100') == 0
assert beginning_zeros('001001') == 2
assert beginning_zeros('012345679') == 1
assert beginning_zeros('0000') == 4

print("Rolou!")

# Tem uns jeitinhos caóticos de resolver isso.
# Solution 02
def beginning_zeros_2(sequence):
    return len(sequence) - len(sequence.lstrip('0'))
# O lstrip() remove tudo que você colocar como argumento da esquerda até encontrar um caractere diferente.
# Por exemplo
# ('fdsafcx').lstrip('adfs') -> 'cx'

print(beginning_zeros_2('100'))
print(beginning_zeros_2('001'))
print(beginning_zeros_2('100010'))
print(beginning_zeros_2('0123'))
print(beginning_zeros_2('0000'))