# SOLUTION 1
def digits_1(number):
    my_number_as_string = str(number)
    return len(my_number_as_string)

# Vamos para o jeito mais caótico?

#SOLUTION 2
import math

def digits_2(number):
    return int(math.log10(number) + 1)

# SOLUTION 3
# Jeito mais rápido!!!!!!!!!!!
from bisect import bisect
K = [0, 
     10, 
     100, 
	 1000, 
	 10000, 
	 100000, 
	 1000000,
     10000000, 
	 100000000, 
	 1000000000,
     10000000000]

def digits_3(n):
    return bisect(K, n)

# Testando
my_number = 342511
print(digits_1(my_number))
print(digits_2(my_number))
print(digits_3(my_number))

from timeit import timeit as t

print(t('digits_1(x)',  setup='x = my_number', number=10000, globals=globals()))  
print(t('digits_2(x)',  setup='x = my_number', number=10000, globals=globals()))  
print(t('digits_3(x)',  setup='x = my_number', number=10000, globals=globals()))  