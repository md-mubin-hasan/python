# fireworks

import random   # module providing the randint function
import time     # time module to delay after drawing five fireworks
import turtle   # turtle module for drawing fireworks
import playsound
#### Initialize variables used in the program

# The following width and height match the GIF used by the program
screen_width, screen_height = 900, 564

firework_radius = 100   # The maximum radius a firework can have
firework_count = 3     # The number of fireworks to shoot

# A list of colours to choose from for a firework
firework_colours = ["red", "orange", "yellow", "green", "cyan", "blue", "violet"]


#### Initialize the turtle module

turtle.setup(screen_width, screen_height)   # Set the size of the screen
turtle.bgpic("Lab 3 - Hong_kong.gif")               # Put the background image on the
                                            # screen
turtle.width(5)                             # Draw lines with a width of three
turtle.shape("circle")                      # Set the turtle to be bomb shape
turtle.color("red")                         # Set the turtle color to red
turtle.speed(6)


#### For loop to shoot individual firework

for i in range(firework_count):
    # Clear the sky (screen) for every five fireworks
    if i > 0 and i % 5 == 0:
        time.sleep(1)
        turtle.clear()

    #### Add your code here
    # Initialize a starting position
    startx = random.randint(int(-(screen_width/2)),int(screen_width/2))
    starty = int(-(screen_height/2))
    # Initialize a destination
    destx = random.randint(int(-(screen_width/2)),int(screen_width/2))
    desty = random.randint(0, int(screen_height/2))
    # Shoot a firework from the start to the destination
    turtle.up()
    turtle.hideturtle()
    turtle.goto(startx, starty)
    turtle.showturtle()
    colour = firework_colours[random.randint(0, len(firework_colours)-1)]
    turtle.color(colour)
    turtle.speed(3)
    turtle.goto(destx, desty)
    turtle.hideturtle()
    turtle.down()

    #### The turtle is in the sky, explode the firework

    #### Add your code here
    # Pick a firework color from the firework colour list
    
    # Pick a size for the firework
    radius = random.randint( int(firework_radius/2), int(firework_radius))
    # Pick the number of explosion directions
    number_directions = random.randint(10,20)
    turtle.up()
    #### For loop to draw each ring of explosion
    dot_size = 1
    playsound.play("Lab 3 - Explosion.wav")
    for this_radius in range(10, radius, 10):
        turtle.tracer(False)
        turtle.setheading(0)
        turtle.forward(this_radius)
        turtle.setheading(90)
        for _ in range(number_directions):
            turtle.circle(this_radius, int(360/number_directions))
            turtle.dot(dot_size)
        turtle.setheading(180)
        turtle.forward(this_radius)
        dot_size = dot_size + 1
        turtle.tracer(True)
    
    #### Add your code here


turtle.done() # Need to keep the window display up
