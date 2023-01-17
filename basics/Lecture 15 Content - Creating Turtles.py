import turtle
import time
import random

def CreateOneTurtle(thiscolor):
    newTurtle = turtle.Turtle()
    newTurtle.shape("turtle")
    newTurtle.color(thiscolor)
    newTurtle.shapesize(2,2)
    newTurtle.up()
    newTurtle.goto(random.randint(-80,80), random.randint(-80,80))
    Allturtles.append(newTurtle)

def ChangeTurtle(TurtleNumber):
    Allturtles[TurtleNumber].left(random.randint(10,95))
    Allturtles[TurtleNumber].forward(random.randint(10,30))
    Allturtles[TurtleNumber].clear()
    Allturtles[TurtleNumber].write(str(Allturtles[TurtleNumber].position()),font=("Arial", 16, "bold"))
    result = Allturtles[TurtleNumber].xcor()
    print("x-cordinate is " + str(result))
    result = Allturtles[TurtleNumber].ycor()
    print("y-cordinate is " + str(result))
    result = Allturtles[TurtleNumber].position()
    print("Position is " + str(result))
    result = Allturtles[TurtleNumber].heading()
    print("Heading is " + str(result))
    result = Allturtles[TurtleNumber].fillcolor()
    print("Fillcolor is " + str(result))
    result = Allturtles[TurtleNumber].shape()
    print("Shape is " + str(result))
    result = Allturtles[TurtleNumber].speed()
    print("Speed is " + str(result))

mubin = turtle.Turtle()
mubin.shape("square")
mubin.shapesize(4,4)
mubin.color("red")
mubin.left(90)
mubin.forward(100)
turtle.forward(100)
time.sleep(1)
mubin.hideturtle()
mubin.clear()
turtle.hideturtle()

Allturtles = []

CreateOneTurtle("red")
CreateOneTurtle("green")
CreateOneTurtle("blue")
CreateOneTurtle("cyan")
CreateOneTurtle("magenta")

while True:
    index = random.randint(0,4)
    ChangeTurtle(index)

turtle.done()
