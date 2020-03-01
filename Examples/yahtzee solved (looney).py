import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 11
# November 14, 2017
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
        for i in self.counts:
            if i == 5:
                return True
    def determineStraight(self):
        x = np.sort(self.rolls)
        flag = False
        for i in range(0, 5):
            if x[i] == i+1:
                flag = True
            else:
                flag = False
                break
        if flag == True:
            return flag
        for i in range(0,5):
            if x[i] == i+2:
                flag = True
            else:
                flag = False
                break
        
        
        return flag
            
        pass
    def determineFullHouse(self):
        for i in self.counts:
            if i == 3:
                for i in self.counts:
                    if i == 2:
                        return True
            
            
        pass
    def getCards(self):
        return self.rolls
    

def main():
    y = Yahtzee()
    full = yah = straight = nothing= 0
##    y.rollDice()
##    y.determineStraight()
    for i in range(2000):
        y.rollDice()
        y.countDiceValues()
        if y.determineYahtzee():
            #print(str(i), "YAHTZEE",  y.getCards())
            yah += 1
        elif y.determineFullHouse():
            #print(str(i), "FullHouse",  y.getCards() )          
            full += 1
        elif y.determineStraight():
            #print(str(i), "Straight", y.getCards())
            straight += 1
        else:
            nothing += 1
    print("Yahtzee", str(yah), "Fullhouse", str(full), "Straights", str(straight), "Losers", str(nothing))     
main()
