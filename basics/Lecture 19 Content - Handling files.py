import turtle
import random

def createTurtles():
    global allTurtles

    for count in range(9):
        newTurtle = turtle.Turtle()
        newTurtle.shape("square")
        newTurtle.shapesize(4,4)
        newTurtle.up()
        newTurtle.speed(0)
        newTurtle.goto(random.randint(-300, 300), random.randint(-300, 300))
        newTurtle.ondrag(newTurtle.goto)
        allTurtles.append(newTurtle)

def savePositions():
    filename = turtle.textinput("Save turtle positions", "What is the filename you want to create?")
    myfile = open(filename, "wt")
    for thisTurtle in allTurtles:
        one_line = str(thisTurtle.xcor()) + "\t" + str(thisTurtle.ycor()) + "\n"
        myfile.write(one_line)
    myfile.close()
    turtle.listen()

def loadPositions():
    global allTurtles

    filename = turtle.textinput("Load turtle positions", "What is the filename you want to load?")
    myfile = open(filename, "r")
    turtleIndex = 0
    for line in myfile:
        line = line.rstrip()
        print("Line is", line)
        items = line.split("\t")
        x = float(items[0])
        y = float(items[1])
        print("x is", x, " y is", y)
        allTurtles[turtleIndex].goto(x, y)
        turtleIndex += 1
    myfile.close()
    turtle.listen()

allTurtles = []
createTurtles()

turtle.onkeypress(savePositions, "s")
turtle.onkeypress(loadPositions, "l")

turtle.listen()
turtle.mainloop()

# This example lines up columns with tab characters

print("Pythagoras' constant is\t1.41421")
print("Theodorus' constant is\t1.73205")
print("Golden ratio is\t\t1.61803")
print("pi is\t\t\t3.14159")
print("e is\t\t\t2.71828")

# This example outputs different numbers of tab characters

for x in range(5):
    print( "\t" * x + "hello")

# This example separates sentences with newline characters

print("Hello!\nI am Python!\nHow are you?")

# This example outputs different numbers of newline characters

for x in range(5):
    print( "hello" + "\n" * x, end="")
