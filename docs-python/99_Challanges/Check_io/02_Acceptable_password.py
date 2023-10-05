from operator import is_


def is_acceptable_password(password):
    if len(password) > 6 :
        return True
    else:
        return False

print(is_acceptable_password("asdf"))

# Muito fácil. Vamos pensar em soluções mais malucas.

# SOLUTION 2
def is_acceptable_password_2(password):
    return len(password) > 6

# SOLUTION 3
is_acceptable_password_3 = lambda password: len(password) > 6


print(is_acceptable_password_2("asdf"))
print(is_acceptable_password_2("asdfasdfasdf"))
print(is_acceptable_password_3("asdf"))
print(is_acceptable_password_3("asdfadsfasfdsa"))