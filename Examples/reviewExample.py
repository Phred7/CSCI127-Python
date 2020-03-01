#########
#Hunter Lloyd
# Question one
########

##score_differences = {}
##score_differences["October 7, 2017"] = 8
##score_differences["October 14, 2017"] = -12
##score_differences["October 21, 2017"] = 3
### The missing code goes here but write it below. Assume that every game results in either a win or a loss.
##wins = losses = 0
##for i in score_differences.values():
##    if i < 0:
##        losses += 1
##    else:
##        wins += 1
##
##print(wins, "wins -", losses, "losses")

#########
#Hunter Lloyd
# Question two
########
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
class Rectangle:
    def __init__(self, p, w, h):
        self.point = p
        self.width = w
        self.height = h

    def getPoint(self):
        return self.point.getX()
    
def main():
    r = Rectangle(Point(4, 5), 6, 5)
    print(r.getPoint())
main()











