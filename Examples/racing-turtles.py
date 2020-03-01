import turtle
import random

window = turtle.Screen()

racer_1 = turtle.Turtle()
racer_1.up()
racer_1.shape("turtle")
racer_1.color(random.random(), random.random(), random.random())
racer_1.goto(-200, 100)
racer_1.down()
racer_1.stamp()

racer_2 = turtle.Turtle()
racer_2.up()
racer_2.shape("turtle")
racer_2.color(random.random(), random.random(), random.random())
racer_2.goto(-200, 0)
racer_2.down()
racer_2.stamp()

for i in range(10):
    racer_1.forward(random.randint(1, 40))
    racer_1.dot()
    racer_2.forward(random.randint(1, 40))
    racer_2.dot()

if racer_1.xcor() > racer_2.xcor():
    print("Turtle racer #1 wins!")
else:
    print("Turtle racer #2 wins!")
                      
                      
window.exitonclick()
    
