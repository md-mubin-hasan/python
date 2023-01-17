import turtle


def drawcircle(x, y):
    turtle.up()
    turtle.goto(0,-180)
    turtle.down()
    turtle.speed(10)
    turtle.circle(180)
def drawstuff(x, y):
    turtle.goto(x,y)
    
turtle.shapesize(2,2)
#turtle.onclick(drawcircle)
turtle.shape("circle")
turtle.color("blue")
turtle.pensize(3)
#turtle.ondrag(drawstuff)
turtle.ondrag(turtle.goto)
turtle.speed(0)

turtle.done()
