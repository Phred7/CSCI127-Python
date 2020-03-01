# --------------------------------------
# CSCI 127, Lab 3
# September 17, 2018
# Walker Ward
# --------------------------------------

def count_vowels(sentence):
    return (sentence.count("a")+sentence.count("e")+sentence.count("i")+sentence.count("o")+sentence.count("u"));

def count_vowels_iterative(s):
    l = len(s);
    x = 0;
    v = 0;
    for i in range(0, l):
        if(s[(x)] == "a" or s[(x)] == "e" or s[(x)] == "i" or s[(x)] == "o" or s[(x)] == "u"):
            v=v+1
        x = x+1;
    return v;

def remove_iterative(x):
    result = "";
    y = 0;
    for i in x:
        if(x[y] == " "):
            result=result;
            #print(result);
        else:
            result=result+i;
            #print(result);
        y=y+1;
    return result;


# --------------------------------------

def main():
    answer = "yes";
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence to evaluate: ");
        sentence = sentence.lower();     # convert to lowercase
        print();
        print("Number of vowels using count     =", count_vowels(sentence));
        print("Number of vowels using iteration =", count_vowels_iterative(sentence));
        print("Using iteration = |" + remove_iterative(sentence) + "|");
        print();
        answer = input("Would you like to continue: ").lower();
        print();
        
# --------------------------------------

main();
