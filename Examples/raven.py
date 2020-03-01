import string

# ---------------------------

def keep_letters(filename):
    file = open(filename, "r")
    modified_text = ""

    for line in file:
        line = line.lower()
        for letter in line:
            if letter in string.ascii_lowercase:
                modified_text += letter

    file.close()
    return modified_text

# ---------------------------

text = keep_letters("raven.txt")
print(text)
        
