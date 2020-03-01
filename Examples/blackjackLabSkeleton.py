
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
    pass

def main():
    ###################
    ##call fillArray above, and fill an array
    ## with ten thousand two card hands
    ## Then below write your code to display the results
    ## in a histogram
    ##################
main()        
