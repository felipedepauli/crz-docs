# min()
# https://medium.com/analytics-vidhya/how-to-use-key-function-in-max-and-min-in-python-1fdbd661c59c

#     1.    Return the smallest item in an iterable or the smallest of two or more arguments.
#     2.    If one positional argument is provided, it should be iterable. The smallest item in the iterable is returned.
#           min(iterable, *[, key, default])
#     3.    If two or more positional arguments are provided, the smallest of the positional arguments is returned.
#           min(arg1, arg2, *args[, key])
#     4.    There are two optional keyword-only arguments.
#     5.    If multiple items are minimal, the function returns the first one encountered. -python docs

#     The key argument specifies a one-argument ordering function. The key function where the iterables are passed and comparison is performed based on its return value
#     The default argument specifies an object to return if the provided iterable is empty. If the iterable is empty and the default is not provided, a ValueError is raised.

mySet = set({1, 2, 10, 3, 9, 22, 90, 100, 20})

print(type(mySet))
print(mySet)
print('-----------')

print(min(mySet))

# Key function

# We can also compare the iterable based on the function specified in the key parameter. It can be

#     Built-in function
#     User-defined function
#     Lambda function
#     itemgetter
#     attrgetter
#Finding largest and smallest key in the dictionary using len()
l1={'carrot':'vegetable','red':'color','apple':'fruit'}
#min() and max() based on len function
print(l1)
print ("Min:", min(l1,key=len))
print ("Max:", max(l1,key=len))

#Finding largest and smallest values in the dictionary based on len()
print('------------')
print ("Min:", min(l1.values(),key=len))
print ("Max:", max(l1.values(),key=len))


def whatIsTheCloser(mySet, reference):
    print(min(mySet, key=lambda element: abs(element - reference)))

whatIsTheCloser(mySet, 19)