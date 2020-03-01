players = {}

class Player:
    
    def __init__(self, inPlayer):
        self.player = inPlayer;
        self.hits = 0;
        self.outs = 0;
        self.bats = 0;
        self.passes = 0;
        self.dErrors = 0;
        self.bAverage = 0;
        self.obPerc = 0;

    def hit(self):
        self.hits += 1;
        self.bats += 1;

    def out(self):
        self.outs += 1;
        self.bats += 1;

    def freePass(self):
        self.passes += 1;
        self.bats += 1;

    def defenceError(self):
        self.dErrors += 1;
        self.bats += 1;
        
    def getCalculations(self):
        x = self.bats-self.dErrors;
        y = self.hits + self.passes + self.dErrors;
        if(x == 0):
            print(self.player, "has no data");
            print();
        else:
            self.bAverage = self.hits/x;
            self.obPerc = y/self.bats;
            print(self.player, "batting average would be", self.hits, "for", x, "or", '{:.3}'.format(self.bAverage));
            print(self.player, "OB% would be", y, "for", self.bats, "or", '{:.3}'.format(self.obPerc));
            print();

def menu():
    print("Options:")
    print("1. Got a hit.");
    print("2. Got out.");
    print("3. Got four balls for a free pass.");
    print("4. Got on base by a defensive error.");
    print("5. Next batter.");
    print();

def user(xBatter, name):
    choice = 0;
    menu();
    while (choice != 5):
        choice = int(input("What did "+name+" do at this bat? "));
        if (choice == 1):
            xBatter.hit();
        elif (choice == 2):
            xBatter.out();
        elif (choice == 3):
            xBatter.freePass();
        elif (choice == 4):
            xBatter.defenceError();
        elif (choice != 5):
            print("That is not a valid option.  Please try again.");


def main():
    name = input("Who is the first batter?");
    print();
    batter = Player(name);
    user(batter, name);
    print();
    name2 = input("Who is the second batter?");
    print();
    batter2 = Player(name2);
    user(batter2, name2);
    print();
    batter.getCalculations();
    print();
    batter2.getCalculations();
    
            
main();
