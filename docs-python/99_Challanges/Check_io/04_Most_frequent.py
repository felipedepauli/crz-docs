data = [ 1, 54, 2, 3, 5, 0, 3, 1, 3, 6, 8, 3, 4, 8, 1, 3, 2, 8, 5, 6, 43, 2, 34, 5, 7, 89, 9, 9, 9, 9, 9]

numbers = dict.fromkeys(set(data), 0)

print(numbers)

for i in data:
    numbers[i] += 1

print(max(numbers, key=numbers.get))

# Dá para fazer algo como no primeiro exemplo, mas muito mais simples
def most_frequent_2(data):
    return max(set(data), key=data.count)

print(most_frequent_2(data))

# Dá para fazer com apenas uma linha.
# CLEANER SOLUTION
from statistics import mode as most_frequent
print(most_frequent(data))
