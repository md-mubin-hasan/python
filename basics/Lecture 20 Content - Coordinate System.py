import turtle

#turtle.setworldcoordinates(0, 0, 1, 1)
#turtle.up()
#turtle.goto(0, 0) #turtle.dot(100) the radius of the dot() does not follow the actual idea of setting up different coordinate system 
#turtle.dot(100)
#turtle.goto(0, 1)
#turtle.dot(100)
#turtle.goto(1, 1)
#turtle.dot(100)
#turtle.goto(1, 0)
#turtle.dot(100)

#turtle.forward(0.5)
#turtle.left(90)
#turtle.forward(0.5)


def draw_rectangle(height):
    for _ in range(2):
        turtle.forward(1)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

values = [7, 2, 8, 10, 6]

turtle.setworldcoordinates(0, 0, 5, 10)

turtle.color("orange")
turtle.speed(0)
turtle.width(5)

for x in range(len(values)):
    turtle.goto(x, 0)
    draw_rectangle(values[x])

turtle.done()
