import turtle

red_turtle_x = 1
green_turtle_x = 2
blue_turtle_x = 3

def red_turtle_drag_handler(x, y):
    red_turtle.ondrag(None)
    x = red_turtle_x
    red_turtle.goto(x, y)
    update_screen_colour()
    red_turtle.ondrag(red_turtle_drag_handler)


def green_turtle_drag_handler(x, y):
    green_turtle.ondrag(None)
    x = green_turtle_x
    green_turtle.goto(x, y)
    update_screen_colour()
    green_turtle.ondrag(green_turtle_drag_handler)


def blue_turtle_drag_handler(x, y):
    blue_turtle.ondrag(None)
    x = blue_turtle_x
    blue_turtle.goto(x, y)
    update_screen_colour()
    blue_turtle.ondrag(blue_turtle_drag_handler)

def update_screen_colour():
    red = min(red_turtle.ycor(), 255)
    green = min(green_turtle.ycor(), 255)
    blue = min(blue_turtle.ycor(), 255)

    red = max(red, 0)
    green = max(green, 0)
    blue = max(blue, 0)

    turtle.bgcolor(int(red), int(green), int(blue))

turtle.colormode(255)
turtle.setworldcoordinates(0,0,4,255)
turtle.hideturtle()

red_turtle = turtle.Turtle()
red_turtle.fillcolor("red")
red_turtle.shape("turtle")
red_turtle.shapesize(4,4,4)
red_turtle.speed(0)
red_turtle.up()
red_turtle.goto(red_turtle_x, 0)
red_turtle.left(90)
red_turtle.ondrag(red_turtle_drag_handler)

green_turtle = turtle.Turtle()
green_turtle.fillcolor("green")
green_turtle.shape("turtle")
green_turtle.shapesize(4,4,4)
green_turtle.speed(0)
green_turtle.up()
green_turtle.goto(red_turtle_x, 0)
green_turtle.left(90)
green_turtle.ondrag(green_turtle_drag_handler)

blue_turtle = turtle.Turtle()
blue_turtle.fillcolor("blue") 
blue_turtle.shape("turtle")
blue_turtle.shapesize(4,4,4)
blue_turtle.speed(0)
blue_turtle.up()
blue_turtle.goto(blue_turtle_x, 0)
blue_turtle.left(90)
blue_turtle.ondrag(blue_turtle_drag_handler)

update_screen_colour()

turtle.done()
