
import numpy as np
import matplotlib.pyplot as plt
import random


def card():
    cardIndex = random.randint(0,12)
    return cardIndex

def deal():
    values = np.array([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
    card1 = card()
    card2 = card()
    total = values[card1] + values[card2]
    return total

def fillArray(howMany):
    ####################
    ## Here you will write the code to call deal and
    ## get a two card hand returned, the values of both cards will
    ## be add together, but you need to deal with two aces....it's easy.
    ## Then return this array to main
    ###################
    array = [];
    for i in range(howMany):
        value = deal();
        if(value == 22):
            value = 12;
        value = value#/howMany
        array.append(value);
    return array;
    


def main():
    ###################
    ##call fillArray above, and fill an array
    ## with ten thousand two card hands
    ## Then below write your code to display the results
    ## in a histogram
    ##################
    plt.figure("CSCI 127 Lab 13");
    plt.axis([3, 22, 0.00, 0.11])
    plt.title("Histogram of Blackjack Hands");
    plt.xlabel("Hand Value");
    plt.ylabel("Probability");
    plt.grid(True);
    plt.xticks(np.arange(4, 22));
    x = fillArray(10000);
    binz = [3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5,19.5,20.5,21.5]
    n = plt.hist(x, bins=binz , density=1, color = "xkcd:cobalt", alpha=0.75);
    plt.show();
main()        
