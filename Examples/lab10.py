import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 10
# November 12, 2018
# Your Name
# -------------------------------------------------

###############
## Class to hold the value of a single die
###############

class Die:

    def __init__(self, sides):
        """A constructor method to create a die"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

# -------------------------------------------------

###############
## Class to hold the value of a single die
###############
class Yahtzee:

    def __init__(self):
        """A constructor method that can record 5 dice rolls"""
        self.rolls = np.zeros(5, dtype=np.int16)

    def rollDice(self):
        """A general method that rolls 5 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(6).roll()

    def countDiceValues(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        self.counts = np.zeros(7, dtype=np.int16)
        for roll in self.rolls:
            self.counts[roll] += 1

    def determineYahtzee(self):
        pass
    def determineStraight(self):
        pass
    def determineFullHouse(self):    
        pass
    def getCards(self):
        return self.rolls
    

def main():
    y = Yahtzee()
    nothing = yahtzeeCount = fullCount= straightCount = 0
    for i in range(200):
        y.rollDice()
        y.countDiceValues()
        ##################
        ####You write your code here and add the code to functions above
        ##########

    print("Yahtzee", str(yahtzeeCount), "Fullhouse", str(fullCount), "Straights", str(straightCount), "Losers", str(nothing))     
main()
