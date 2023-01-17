import turtle

def moveforward():
    turtle.forward(5)
def movebackward():
    turtle.backward(5)
def rotateleft():
    turtle.left(5)
def rotateright():
    turtle.right(5)

def orange():
    turtle.color("orange")
def red():
    turtle.color("red")
def cyan():
    turtle.color("cyan")
def green():
    turtle.color("green")

def jump(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

turtle.speed(0)
turtle.width(3)
#turtle.pensize(3)
#Fill the turtle with no colour
#turtle.fillcolor("") 

turtle.onkeypress(moveforward, "Up")
turtle.onkeypress(movebackward, "Down")
turtle.onkeypress(rotateleft, "Left")
turtle.onkeypress(rotateright, "Right")

turtle.onkeypress(orange, "o")
turtle.onkeypress(red, "r")
turtle.onkeypress(cyan, "c")
turtle.onkeypress(green, "g")


turtle.onscreenclick(jump)

turtle.listen()
turtle.done()
