#  Find the nearest value to the given one.

# You are given a list of values as set form and a value for which you need to find the nearest one.

# For example, we have the following set of numbers: 4, 7, 10, 11, 12, 17, and we need to find the nearest value to the number 9. If we sort this set in the ascending order, then to the left of number 9 will be number 7 and to the right - will be number 10. But 10 is closer than 7, which means that the correct answer is 10.

# A few clarifications:

#     If 2 numbers are at the same distance, you need to choose the smallest one;
#     The set of numbers is always non-empty, i.e. the size is >=1;
#     The given value can be in this set, which means that it’s the answer;
#     The set can contain both positive and negative numbers, but they are always integers;
#     The set isn’t sorted and consists of unique numbers.


# Solution 01
def nearest_value_1(values, one):
    my_list = list(values)
    my_list.sort()
    if one in my_list:
        return one
    if len(my_list) == 1 or one < my_list[0]:
        return my_list[0]
    if one > my_list[-1]:
        return my_list[-1]
    

    my_list.append(one)
    my_list.sort()
    index = my_list.index(one)
    if abs(my_list[index] - my_list[index-1]) <= abs(my_list[index+1] - my_list[index]):
        return my_list[index-1]
    else:
        return my_list[index+1]

# Solution 02
def nearest_value_2(values: set, one: int) -> int:
    return min(values, key=lambda n: (abs(one - n), n))

# Solution 03
import numpy as np
def nearest_value_3(values: set, one: int) -> int:
    value_list = np.array(list(values))
    value_list.sort()
    index = abs(value_list - one).argmin()
    return value_list[index]


print(nearest_value_1({1, 2, 3, 4, 5, 6, 7, 8, 9, 40, 50, 80, 100}, 20))
print(nearest_value_2({1, 2, 3, 4, 5, 6, 7, 8, 9, 40, 50, 80, 100}, 20))