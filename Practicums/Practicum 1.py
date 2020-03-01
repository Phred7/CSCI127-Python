import turtle

def imprint(turtle, x, y, color):
    turtle.up();
    turtle.color(color);
    turtle.goto(x, y);
    turtle.stamp();

some_turtle = turtle.Turtle();
some_turtle.shape("turtle");
some_turtle.hideturtle();

imprint(some_turtle, 0, 0, "red");
imprint(some_turtle, 100, -50, "blue");
imprint(some_turtle, -75, -25, "purple");
