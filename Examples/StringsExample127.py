
def reverse(x):
    result = ""
    for i in x:
        result = i + result
    return result


def eliminate(word, letter):
    result = word.replace(letter, "")
    return result

def letsStrip(word):
    result = word.replace(" ", "")
    return result


def main():
    mascot = "Hawks!"
    print(mascot[1:])
    print('A' == 'a')
      


    #word = "hunter"
    #print(len(word))
##    print(word.upper())
##    print(word.capitalize())
##    print(eliminate("blue bubble boy", "b"))
##    print(letsStrip("  blue bubble boy  !"))
##    print(reverse("Hunter"))

main()
