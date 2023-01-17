import turtle
import random
turtle.speed(0)
#turtle.width(20)
colors = ["blue", "green", "red"]

turtle.color("green")
turtle.up()
turtle.goto(100, -400)
turtle.left(90)
turtle.down()
turtle.circle(1000, 30)
turtle.up()
turtle.goto(0, 0)
count = 0
petals = int(input("How many petals do you want? "))
turtle.hideturtle()

while count < petals:
    #turtle.color(random.choice(colors))
    turtle.circle(100)
    turtle.left(360/petals)
    count = count + 1

turtle.done()
