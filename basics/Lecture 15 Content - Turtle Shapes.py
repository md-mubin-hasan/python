import turtle
# Clear the screen and draw a square
def draw():
    turtle.clear()
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

# Change the turtle shape to 'arrow'
def arrow_shape():
    turtle.shape("arrow")
    draw()

# Change the turtle shape to 'circle'
def circle_shape():
    turtle.shape("circle")
    draw()

# Change the turtle shape to 'triangle'
def triangle_shape():
    turtle.shape("triangle")
    draw()

# Change the turtle shape to 'turtle'
def turtle_shape():
    turtle.shape("turtle")
    draw()

# Change the turtle shape to 'square'
def square_shape():
    turtle.shape("square")
    draw()

# Change the turtle shape to 'classic'
def classic_shape():
    turtle.shape("classic")
    draw()

# Change the turtle shape to a GIF image
def gif_shape():
    turtle.addshape("ninja_small.gif")
    turtle.shape("ninja_small.gif")
    draw()

# Start of the main program
print("Repeatedly press Enter to see a new shape")
# Change the turtle shape to a turtle and use red colour
turtle.shape("turtle")
turtle.color("red")

# Get the user input for the width and length of the turtle shape
width = input("Enter the width of the shape: ")
length = input("Enter the length of the shape: ")

# Change the size according to the input values
turtle.shapesize(float(width), float(length))

arrow_shape()
input("Press Enter")

circle_shape()
input("Press Enter")

triangle_shape()
input("Press Enter")

turtle_shape()
input("Press Enter")

square_shape()
input("Press Enter")

classic_shape()
input("Press Enter")

gif_shape()
input("Press Enter")

turtle.done()

#turtle shape default is classic
turtle.speed(10)

turtle.shapesize(5,5)
turtle.shape("arrow")
turtle.circle(100)

turtle.shape("turtle")
turtle.circle(100)

turtle.shape("circle")
turtle.circle(100)

turtle.shape("square")
turtle.circle(100)

turtle.shape("triangle")
turtle.circle(100)

turtle.shape("classic")
turtle.circle(100)

turtle.shapesize(5,5)  #(width, length)
#shapesize doesn't change the size of the gif image
turtle.addshape("ninja_small.gif")
turtle.shape("ninja_small.gif")
turtle.circle(100)

turtle.done()

