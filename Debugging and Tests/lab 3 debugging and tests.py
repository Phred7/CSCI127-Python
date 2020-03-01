##sentence = input("Please enter a sentence to evaluate: ");
##sentence = sentence.lower();     # convert to lowercase
##print(sentence.count("a")+sentence.count("e")+sentence.count("i")+sentence.count("o")+sentence.count("u"));

##def count_vowels_iterative(s):
##    l = len(s);
##    x = 0;
##    v = 0;
##    for i in range(0, l):
##        print(x);
##        if(s[(x)] == "a" or s[(x)] == "e" or s[(x)] == "i" or s[(x)] == "o" or s[(x)] == "u"):
##            v=v+1
##        else:
##            print(False);
##        x = x+1;
##    return v;
##
##s = "aeioua";
##v = count_vowels_iterative(s);
###print(s[0])
##print("v", v);

def remove_iterative(x):
    sTR = x.strip();
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
        
x = " h i there p"
print(remove_iterative(x));
