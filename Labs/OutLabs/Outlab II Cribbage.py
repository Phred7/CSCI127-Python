# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program II: Cribagge Hand Calculator 
# Walker Ward
# Last Modified: October 8, 2018 
# ---------------------------------------
# Calculates points in a 3-card cribbage
# hand. Imports and reads data from a .txt
# file for hand inputs
# ---------------------------------------

def evaluate_hand(hand_as_list): ##gathers information from hand_as_list and calls each function to determine the points per hand
    points = 0;
    cards = [];
    num1, card1 = hand_as_list[0];
    num2, card2 = hand_as_list[1];
    num3, card3 = hand_as_list[2];
    cards.append(int(num1));
    cards.append(int(num2));
    cards.append(int(num3));
    cards.sort();
    x = num1 + num2 + num3;
    y = x - num1;
    z = x - num2;
    za = x - num3;
    points = threeKind(points, num1, num2, num3) + pair(points, num1, num2, num3) + sequence(points, cards) + fifteens(points, x, y, z, za);
    return points;

def threeKind(points, num1, num2, num3): ##this function determines if the cards are three of a kind (numerically)
    if(num1 == num2 == num3): 
        points = points + 6;
    return points;

def pair(points, num1, num2, num3): ##this function determines if there are any pairs
    if(num1 == num2 == num3):
        return points;
    if(num1 == num2 or num2 == num3 or num1 == num3): ##pair
        points = points + 2;
    return points;

def sequence(points, c): ##this function determines if the cards are in a sequence
    cards = c;
    if((cards[1] == (int(cards[0] + 1))) and (cards[2] == (int(cards[1] + 1)))): 
        points = points + 3;
    return points;

def fifteens(points, x, y, z, za): ##this function determines if the cards sum up to 15 in any way
    if(x == 15):
        points = points + 2;
    if(y == 15):
        points = points + 2;
    if(z == 15):
        points = points + 2;
    if(za == 15):
        points = points + 2;
    else:
        points = points;
    return points;
    

def print_hand(hand_as_list): ##this function prints each hand based on the output format and grabs info from the evaluate hand function
    points = 0;
    print("Cribbage Hand");
    print("-------------");
    points = evaluate_hand(hand_as_list);
    for i in range(3):
        cardN = i + 1;
        num, card = hand_as_list[i];
        card = card.capitalize();
        print("Card", str(cardN)+":", num, "of", card);
    print("Points scored:", points);
    print("");

# --------------------------------------
# Change everything below this line!
# --------------------------------------

def process_hands(cribbage_input, cards_in_hand):    

    for hand in cribbage_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([int(hand[0]), hand[1]])
            hand = hand[2:]
        print_hand(hand_as_list)
        evaluate_hand(hand_as_list)

# --------------------------------------

def main():
    cribbage_file = open("cribbage.txt", "r")
    process_hands(cribbage_file, 3)
    cribbage_file.close()

# --------------------------------------

main()
