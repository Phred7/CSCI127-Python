
def count_vowels_iterative(sentence):
    total = 0
    vowels = ["a","e","i","o","u"]
    for vowel in vowels:
        total += sentence.count(vowel)
    return(total)

print(count_vowels_iterative("hoot umb celi"))
