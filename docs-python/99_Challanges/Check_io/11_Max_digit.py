# Solution 1
def max_digit_1(number):
    number_as_string = str(number)
    number_as_array  = (int(i) for i in number_as_string)
    return max(number_as_array)

number = 1934551
print("Solution 1:", max_digit_1(number))

# Em uma linha?
# Solution 2
max_digit_2 = lambda number: max(int(i) for i in str(number))
print("Solution 2:", max_digit_2(number))

# Tem um muito legal, que com certeza será mais rápido. Vamos lá.
# SOLUTION 3
def max_digit_3(number):
    for i in range(10)[::-1]:
        if str(i) in str(number):
            return i
    return 0

print("Solution 3:", max_digit_3(number))

# Vamos testar a velô:
from timeit import timeit as t

print(t('max_digit_1(x)', setup='x = 1010101020201010101011010101010109', number=10000, globals=globals()))       #  ~1.53 ms
print(t('max_digit_2(x)', setup='x = 1010101020201010101011010101010109', number=10000, globals=globals()))       #  ~1.44 ms
print(t('max_digit_3(x)', setup='x = 1010101020201010101011010101010109', number=10000, globals=globals()))       #  ~0.02 ms
# Diferença?

# Mais um
# SOLUTION 4
def max_digit_4(number: int) -> int:
    return max(map(int, str(number)))

print(t('max_digit_4(x)', setup='x = 1010101020201010101011010101010109', number=10000, globals=globals()))       #  ~0.02 ms
