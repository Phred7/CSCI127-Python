import turtle
import random

window = turtle.Screen();

square = turtle.Turtle();
square.speed(0);
square.hideturtle();

square.up();
square.goto(-200, 200);
square.down();

for i in range(4):
    square.forward(50);
    square.right(90);

square.up();
square.goto(-205, 205);
square.write("Change Color");

##first square end

square.up();
square.goto(150, 200);
square.down();

for i in range(4):
    square.forward(50);
    square.right(90);

square.up();
square.goto(145, 205);
square.write("Move Mouse");

##second square end

pencil = turtle.Turtle();
pencil.shape("circle");
pencil.speed(9);

##print("x, y");

def drawingControls(x, y):
    if (-200 <= x <= -150) and (150 <= y <= 200):
        red = random.random();
        green = random.random();
        blue = random.random();
        pencil.color(red, green, blue);
        #change color
        
    if (150 <= x <= 200) and (150 <= y <= 200):
        x = random.randrange(750);
        y = random.randrange(600);
        x = x - 375;
        y = y - 300;
        ##print(x, y)
        pencil.goto(x, y);
        #move turtle

window.onclick(drawingControls);

pencil.onrelease(pencil.goto);




