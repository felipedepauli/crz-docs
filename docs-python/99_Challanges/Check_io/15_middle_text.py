#  You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.

# This is a simplified version of the Between Markers mission.

#     The initial and final markers are always different.
#     The initial and final markers are always 1 char size.
#     The initial and final markers always exist in a string and go one after another.

# Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

# Output: A string.

# Solution 01:

def middle_text(text, a, b):
    text2 = ""
    control = False
    for letter in text:
        if letter == a and control == False:
            control = True
            continue
        if control:
            if letter == b:
                break
            else:
                text2 += letter
    return text2

print(middle_text("Meu <sapato é <azul>", "<", ">"))

# Solution 02:
def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    return text[text.index(begin)+1:text.index(end)]

# Solution 03:
def between_markers(text, begin, end):
    i = text.find(begin) + 1
    j = text.find(end, i)
    return text[i:j]