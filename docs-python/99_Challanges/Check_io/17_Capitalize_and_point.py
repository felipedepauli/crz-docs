#  For the input of your function, you will be given one sentence. You have to return a corrected version, that starts with a capital letter and ends with a period (dot).
# Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a period (dot), then adding another one will be a mistake.
# Input: A string.
# Output: A string. 

def correct_sentence(text):
    text = str(text)
    text_splitted = text.split(" ")[0].split(",")[0].capitalize()
    if text[-1] != ".":
        text += "."
    return text_splitted[0] + text[1:]
        
    

print(correct_sentence("vc é doidão!"))