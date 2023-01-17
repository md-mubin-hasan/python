# Introduction to Turtle Graphics
import turtle
turtle.speed(6) # Speed of 0 is very fast
#speed of 1 is very slow, speed of 6 is normal and speed of 10 is fast
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.color("blue")
turtle.backward(100)
turtle.left(90)
turtle.backward(100)
turtle.right(90)
turtle.forward(200)
turtle.color('red') #changes both pen and fill color
#turtle.color("blue", "red") here blue is pencolor and red is fill color
turtle.width(5)
turtle.forward(200)
turtle.clear()
turtle.goto(0,0)
turtle.up()
turtle.penup() #same as turtle.up()
turtle.clear()
turtle.left(90)
turtle.write("Mubin")
turtle.write("COMP1021", font = ("Arial", 20, "bold"))

turtle.pencolor("orange")
turtle.fillcolor("purple")
turtle.forward(100)
turtle.backward(100)
turtle.pendown() #same as turtle.down()
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)

turtle.begin_fill()
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.end_fill()
# turtle.clear()
turtle.up()
turtle.hideturtle() #turtle symbol is hidden.
#turtle.showturtle() is used to unhide

turtle.goto(0,0)
turtle.right(120)
turtle.right(120)
turtle.circle(100)
turtle.down()
turtle.circle(100)
turtle.circle(-100)
turtle.circle(10)
turtle.circle(-10)
turtle.circle(50, 90) #radius is 50 and the angle of sector is 90 degree
turtle.circle(50, 180)
turtle.st()   #this unhides the turtle
#turtle.showturtle()

# turtle.dot(any number) will make a filled circle
turtle.done() #this is needed when we do advanced stuff
#this is used to tell Python that we are done with drawing

