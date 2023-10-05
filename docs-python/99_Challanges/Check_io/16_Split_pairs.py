# Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').
# Input: A string.
# Output: An iterable of strings. 

# Solution 01
def split_pairs_1(string):
    if len(string) % 2 == 1:
        string += "_"
    return [string[i:i+2] for i in range(0, len(string), 2)]

print(split_pairs_1("abcdef"))

# Solution 02
def split_pairs_2(a):
    return [ch1+ch2 for ch1,ch2 in zip(a[::2],a[1::2]+'_')]

