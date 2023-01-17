# COMP1021 Lab 2 Python Sketchbook
# Name: HASAN, Md Mubin
# Student ID: 20901262
# Email: mmhasanaa@connect.ust.hk

import turtle       # Import the turtle module for the program

turtle.width(4)
turtle.speed(10)

##### Initialize the colour
fillcolor = "black"
turtle.pencolor("black")
turtle.fillcolor(fillcolor)

print("Welcome to the Python Sketchbook!")

##### While loop to repeat the main menu

# Initialize the option to empty in order to enter the while loop
option = ""


while option != "q": # While the option is not "q"
    print()
    print("Please choose one of the following options:")
    print()
    print("m - Move the turtle")
    print("t - Rotate the turtle")
    print("l - Draw a line")
    print("r - Draw a rectangle")
    print("c - Draw a circle")
    print("p - Change the pen colour of the turtle")
    print("f - Change the fill colour of the turtle")
    print("g - Draw a generated flower")
    print("e - Draw a generated explosion")
    print("a - Draw the author's information")
    print("q - Quit the program")
    print()

    option = input("Please enter your option: ")

    ##### Handle the move option
    if option == "m":
        print()

        # Ask the user for the x and y value
        x = input("Please enter the x value: ")
        x = int(x)
        y = input("Please enter the y value: ")
        y = int(y)

        # Move the turtle without drawing anything
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

    ##### Handle the rotate option
    if option == "t":
        print()

        #
        # Please put your code here
        angle = int(input("Please enter the angle of rotation: "))
        turtle.left(angle)
        #

    ##### Handle the line option
    if option == "l":
        print()

        # Ask the user for the x and y value
        x = input("Please enter the x value: ")
        x = int(x)
        y = input("Please enter the y value: ")
        y = int(y)

        # Move the turtle and draw a line
        turtle.goto(x, y)

    ##### Handle the rectangle option
    if option == "r":
        print()

        #
        # Please put your code here
        width = input("Please enter the width of the rectangle: ")
        width = int(width)
        height = input("Please enter the height of the rectangle: ")
        height = int(height)
        turtle.begin_fill()
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.end_fill()
        #

    ##### Handle the circle option
    if option == "c":
        print()

        #
        # Please put your code here
        radius = input("Please enter the radius of the circle: ")
        radius = int(radius)
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        #

    ##### Handle the pen colour option
    if option == "p":
        print()

        #
        # Please put your code here
        pen_color = input("Please enter a colour name for the pen colour: ")
        turtle.pencolor(pen_color)
        #

    ##### Handle the fill colour option
    if option == "f":
        print()

        #
        # Please put your code here
        fillcolor = input("Please enter a colour name for the fill colour: ")
        turtle.fillcolor(fillcolor)
        #
    ##### Handle the generate flower option
    if option == "g":
        print()

        #
        # Please put your code here
        petal = int(input("Please enter the size of the flower petal: "))
        for _ in range(12):
            for __ in range(3):
                turtle.forward(petal)
                turtle.left(120)
            turtle.left(30)
        #
    ##### Handle the generated explosion
    if option == "e":
        print()

        #
        # Please put your code here
        size = int(input("Please enter the size of the explosion (>=160): "))
        oldpencolor = turtle.pencolor()
        oldfillcolor = turtle.fillcolor()

        for thiscolor in ["sienna", "brown",  \
                  "red", "dark orange", "orange","gold2", "gold", "yellow"]: 
            turtle.color(thiscolor)
            turtle.dot(size)
            size = size - 10
    
        turtle.pencolor(oldpencolor)
        turtle.fillcolor(oldfillcolor)
        #
    ##### Handle the author's information
    if option == "a":
        print()

        #
        # Please put your code here
        turtle.up()
        turtle.backward(200)
        turtle.down()
        turtle.left(90)
        turtle.forward(80)
        turtle.right(130)
        turtle.forward(30)
        turtle.left(80)
        turtle.forward(30)
        turtle.right(130)
        turtle.forward(80)
        turtle.left(90)
        
        turtle.up()
        turtle.forward(10)
        turtle.down()
        
        turtle.left(90)
        turtle.forward(80)
        turtle.backward(80)
        turtle.right(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(80)
        turtle.backward(80)
        turtle.right(90)
        
        turtle.up()
        turtle.forward(10)
        turtle.down()
        
        turtle.circle(20, 180)
        turtle.right(180)
        turtle.circle(20, 180)
        turtle.left(90)
        turtle.forward(80)
        turtle.left(90)
        
        turtle.up()
        turtle.forward(30)
        turtle.down()
        
        turtle.left(90)
        turtle.forward(80)
        turtle.backward(80)
        turtle.right(90)
        turtle.up()
        turtle.forward(10)
        turtle.down()
        turtle.left(90)
        turtle.forward(80)
        turtle.right(120)
        turtle.forward(160)
        turtle.left(120)
        turtle.forward(80)

        turtle.up()
        turtle.right(90)
        turtle.goto(0,0)
        turtle.down()
turtle.done()
