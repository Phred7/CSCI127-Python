import turtle
import numpy as np
import random
# --------------------------------------
class House():
    def __init__(self):
        window = turtle.Screen()
        window.colormode(255)
        self.cecil = turtle.Turtle()
        self.drawNeighborhood()
        window.exitonclick()


    def drawHouse(self, coordinates, pen_color):
        self.cecil.fillcolor(pen_color)
        self.cecil.up()
        self.cecil.goto(coordinates[0][0], coordinates[0][1])
        self.cecil.down()
        #self.cecil.speed(1)
        self.cecil.begin_fill()
        for coordinate in coordinates[:5]:
            self.cecil.goto(coordinate[0], coordinate[1])
        self.cecil.end_fill()
        self.cecil.fillcolor("brown")
        self.cecil.begin_fill()
        for coordinate in coordinates[5:]:
            self.cecil.goto(coordinate[0], coordinate[1])
        self.cecil.end_fill()
# --------------------------------------

    def drawNeighborhood(self):
        self.cecil.hideturtle()
        coordinates = np.array([[-30, 50], [-30, -50], [70, -50], [70, 50],
                                [-30, 50], [20, 100], [70, 50]])
        
##        self.drawHouse(coordinates, "black")
##        #input("+10")
##        self.drawHouse(coordinates + 10, "black")
##        #input("+[-100, -200]")
##        self.drawHouse(coordinates + [-100, -200], "red")
##        #input("*2")
##        self.drawHouse(coordinates * 2, "turquoise")
##        #input("* .5, .2")
##        self.drawHouse(coordinates * [.5, .2] + [100, 200], "blue")
        offset = np.array([-300, -200])
        for i in range(1,6):
            self.drawHouse(coordinates + offset, (random.randint(0,255), random.randint(0,255), random.randint(0,255)) )
            offset = offset + [110, 0]
        offset = np.array([-300, -50])
        for i in range(1,6):
            self.drawHouse((coordinates + offset)*.8, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            offset = (offset + [110,0 ])   

# --------------------------------------

def main():
   house = House()

main()
