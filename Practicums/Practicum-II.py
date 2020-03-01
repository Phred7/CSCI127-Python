############
#Walker Ward
#CSCI 127 Practicum II
#10/31/18
############

############
#Question I
############

##
##def determineColors(dic):
##    g = b = r = o = 0;
##    for values in dic.values():
##        if(values == "green"):
##            g += 1;
##        elif(values == "blue"):
##            b += 1;
##        elif(values == "red"):
##            r += 1;
##        else:
##            o += 1;
##    return "green = {}, blue = {}, red = {}, other = {}".format(g, b, r, o);
##    
##def main():
##    trains = {};
##    trains["Percy"] = "green";
##    trains["Thomas"] = "blue";
##    trains["James"] = "red";
##    trains["Nia"] = "yellow";
##    trains["Gordon"] = "blue";
##    trains["Emily"] = "green";
##    trains["Duck"] = "green";
##    print(determineColors(trains));
##
##main();
##

############
#Question II
############

##class Square():
##    def __init__(self, coord , length):
##        self.x = coord[0];
##        self.y = coord[1];
##        self.l = length;
##    def getX(self):
##        return self.x;
##    def getY(self):
##        return self.y;
##    def getLength(self):
##        return self.l;
##    def compare(self, objectII):
##        if(objectII.getX() + objectII.getLength() < self.x):
##            return "Left";
##        if(objectII.getX() > self.x + self.l):
##            return "Right";
##        if(objectII.getX() + objectII.getLength() > self.x and objectII.getY() - objectII.getLength() < self.y):
##            return "Overlap";
##        
##def main():
##    pacman = Square((25, 25), 50);
##    second = Square((5, 11), 10);
##    print("Second:", pacman.compare(second));
##    third = Square((5, 21), 30);
##    print("Third:", pacman.compare(third));
##    fourth = Square((80, 31), 10);
##    print("Fourth:", pacman.compare(fourth));
##    
##main();
##
