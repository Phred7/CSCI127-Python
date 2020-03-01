import turtle

arbC = 5;
t = turtle.Turtle();
t.speed(0);
t.hideturtle();

def double(x, y, l, w):
    for i in range(2):
        if(i == 0):
            pixel(x+1, y, l, w);
        elif(i == 1):
            pixel(-x, y, l, -w);
    
def pixel (x, y, l, w):
    l = l * arbC;
    w = w * arbC;
    x = x * arbC;
    y = y * arbC;
    t.up();
    t.goto(x,y);
    t.down();
    t.begin_fill();
    for i in range(4):
        if(i%2 == 0):
            t.forward(w);
        elif(i%2 != 0):
            t.forward(l);
        t.right(90);
    t.end_fill();

def outlineBKGD(t):
    
    t.color("silver");
    pixel(-8, 1, 8, 17); ##face
    double(6, 6, 5, 2);
    double(1, 2, 1, 1);
    double(5, 2, 1, 1);
    t.color("dodgerblue");
    pixel(-12, 12, 6 ,24);
    double(8, 11, 14, 3);
    double(-4, 14, 2, 12);
    #double(
    t.color("steelblue");
    double(-13, -5, 4, 9);
    double(-11, -3, 2, 5);
    t.color("silver");
    pixel(-1, 10, 10, 3);
    pixel(-6, 9, 3, 13);
    double(3, -5, 1, 1);
    t.color("dimgrey");
    pixel(-14, -10, 2, 28);
    t.color("dodgerblue");
    double(5, 9, 1, 1);
    t.color("red");
    pixel(-14, -13, 3, 28);
    t.color("black");
    double(11, 12, 18, 1); ## sides (long)
    double(12, -5, 4, 1);
    double(13, -9, 8, 1);
    for i in range(2):
        pixel(-13, -9-(3*i), 1, 28);
    pixel(-13, -16, 1, 28);
    double(10, 12, 1, 1);
    for i in range(3):
        double(8-(4*i), 13+i, 1, 4);
    double(-2, -12, 5, 1);
    pixel(0, -10, 2, 1); 
    pixel(-2, 16, 6, 5); ##stack
    double(1, 10, 1, 3); ##face circle
    for i in range(3):
        double(4+i, 9-i, 1, 1);
    double(7, 6, 3, 1);
    double(8, 4, 5, 1);
    double(7, 0, 3, 1);
    for i in range(3):
        double(6-i, -2-i, 2, 1);
    double(3, -6, 1, 1);
    pixel(-4, -7, 3, 9);
    double(8, -2, 1, 2);
    double(9, -3, 1, 1);
    double(10, -3, 2, 1);
    pixel(-11, -10, 2, 1);
    pixel(-6, -10, 2, 1);
    pixel(5, -10, 2, 1);
    pixel(10, -10, 2, 1);
    
def eyes(t):
    t.color("black");
    double(5, 6, 1, 1); ##brows
    double(1, 6, 1, 1); ##brows
    double(2, 7, 1, 3); ##brows
    double(3, 5, 1, 1); ##pupil
    double(2, 4, 2, 3); ##pupil
    t.color("dimgrey");
    double(2, 1, 1, 1); ##creases
    double(6, 1, 1, 1);
    double(3, 0, 1, 3);
    double(4, -1, 1, 1); 
    
def lights(t):
    t.color("yellow");
    for i in range(3): ##could use a factorial
        double(7-i, 12-i, 1, 2+(2*i));
    double(6, 9, 1, 4);
    double(7, 8, 1, 2);
    t.color("black");
    for i in range(2):
        double(7-i, 11-i, 1, 2+(2*i));
    double(7, 9, 1, 2);
    
def nose(t):
    t.color("dimgrey");
    pixel(-1, 2, 2, 1);
    pixel(0, 2, 3, 1);
    pixel(1, 1, 2, 1);

def mouth(t):
    t.color("black");
    pixel(-4, -2, 1, 9); ##top
    pixel(-2, -4, 1, 5); ##bottom
    double(2, -3, 1, 1); ##mid
    t.color("white");
    pixel(-2, -3, 1, 5);

def stops(t):
    t.color("black");
    double(5, -14, 1, 4);
    for i in range(3):
        double(4, -15-i, 1, 6);
    double(5, -18, 1, 4);
        
        
def screen():
    screen = turtle.Screen();
    screen.bgcolor("white");
    screen.screensize(31*arbC, 36*arbC);

def main():
    screen();
    outlineBKGD(t);
    nose(t);
    eyes(t);
    mouth(t);
    lights(t);
    stops(t);

main();


