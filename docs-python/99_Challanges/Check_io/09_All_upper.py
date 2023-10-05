def isAllUpper_1(s):
    return s == s.upper()

def isAllUpper(s):
    return all(c.isupper() for c in s)

print(isAllUpper_1('HELLO'))

print(isAllUpper('HELLO'))