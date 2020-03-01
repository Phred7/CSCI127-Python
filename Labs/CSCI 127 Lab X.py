import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 10
# November 12, 2018
# Walker Ward
# This program is designed to run a simplified
# simulation of the game "Yahtzee". In 200 rolls
# this program will randomly generate dice throws
# and calculate straights, yahtzees and full houses
# compared to the number of losses and return any
# wins to the terminal with the rolls.
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
        if(self.rolls[0] == self.rolls[1] == self.rolls[2] == self.rolls[3] == self.rolls[4]):
            return True;
        else:
            return False;
    def determineStraight(self):
        a = self.rolls;
        aa = a.copy();
        aa.sort();
        b = np.array([1, 2, 3, 4, 5]);
        c = np.array([2, 3, 4, 5, 6]);
        if(aa[0] == b[0] and aa[1] == b[1] and aa[2] == b[2] and aa[3] == b[3]  and aa[4] == b[4] or aa[0] == c[0] and aa[1] == c[1] and aa[2] == c[2] and aa[3] == c[3]  and aa[4] == c[4]):
            return True;
        else:
            return False;
    def determineFullHouse(self):
        a = self.rolls.copy();
        a.sort();
        if((a[0] == a[1] == a[2] and a[3] == a[4]) or (a[1] == a[2] == a[3] and a[0] == a[4]) or (a[2] == a[3] == a[4]) and a[0] == a[1]):
            return True;
        else:
            return False;
    def getCards(self):
        return self.rolls
    

def main():
    y = Yahtzee()
    nothing = yahtzeeCount = fullCount = straightCount = 0
    for i in range(200):
        y.rollDice()
        y.countDiceValues()
        if(y.determineYahtzee() == True):
            print(i, "Yahtzee", y.getCards());
            yahtzeeCount += 1;
        elif(y.determineStraight() == True):
            print(i, "Straight", y.getCards());
            straightCount += 1;
        elif(y.determineFullHouse() == True):
            print(i, "FullHouse", y.getCards());
            fullCount += 1;
        nothing = 200 - yahtzeeCount - fullCount - straightCount;

    print("Yahtzee", str(yahtzeeCount), "Fullhouse", str(fullCount), "Straights", str(straightCount), "Losers", str(nothing))     
main()

