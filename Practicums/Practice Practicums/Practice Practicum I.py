import turtle


def bobcat_line(turtle, nS, sL):
    eo = 0;
    for i in range(nS):
        if(eo%2 == 0):
            #x = turtle.getx;
            turtle.color('blue');
            turtle.forward(sL);
            
            #drawing_turtle.
        elif(eo%2 != 0):
            turtle.color('gold');
            turtle.forward(sL);
        eo=eo+1;
            
# The missing function goes here but write it below.
drawing_turtle = turtle.Turtle()
drawing_turtle.width(3)
drawing_turtle.hideturtle()
number_segments = int(input("Enter number of segments: ")) # Assume the user will enter an integer >= 1
segment_length = int(input("Enter length of a segment: ")) # Assume the user will enter an integer >= 10
bobcat_line(drawing_turtle, number_segments, segment_length)
