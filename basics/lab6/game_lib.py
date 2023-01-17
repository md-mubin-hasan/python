#
# THE CONTENT OF THIS FILE WON"T BE TAUGHT IN THE LAB.
# YOU ARE NOT EXPECTED TO UNDERSTAND THE CONTENT OF THIS FILE.
#

import turtle
import game_map

#
# The following are the global variables used by the game
#

# The map is stored as a list of lists structure
game_map_data = []

# These variables store the size (number of rows and columns) of the game map
game_map_total_rows = 0
game_map_total_cols = 0

# These variables store the current location (row and column) of the robot
robot_row = 0
robot_col = 0

# This variable is True when the game finishes, i.e. the robot reaches the exit
# or False otherwise
is_finished = False

# This variable is True when the robot cannot see the rest of the map, or False otherwise
robot_view = False

# This variable stores the decision making function and timing
timing = 200
current_task_handler = None

task_handlers = {"task0":None,"task1":None,"task2":None,"task3":None,"task4":None}

currentTask = None

total_width = 500
total_height = 500

a_block_width = 500
a_block_height = 500

turtle.colormode(255)

drawing_turtles = []
layer2_drawing_turtles = []

forceUpdate = False

#
# The following 8 functions are available to help make the robot's decision
#


# This function returns True if a wall is above the robot
# or False otherwise
def northIsWall():
    return game_map_data[robot_row-1][robot_col] == "B"

# This function returns True if a wall is below the robot
# or False otherwise
def southIsWall():
    return game_map_data[robot_row+1][robot_col] == "B"

# This function returns True if a wall is on the east of the robot
# or False otherwise
def eastIsWall():
    return game_map_data[robot_row][robot_col+1] == "B"

# This function returns True if a wall is on the west of the robot
# or False otherwise
def westIsWall():
    return game_map_data[robot_row][robot_col-1] == "B"


# This function lets you choose the game map to start the game from
def chooseGameMap(task, map_number):
    global currentTask
    global game_map_data
    global game_map_total_rows, game_map_total_cols
    global robot_row, robot_col
    global a_block_width, a_block_height
    
    currentTask = task

    # Get the 'raw' game map containing a big string
    if task != "custom":
        raw_game_map_data = game_map.getGameMap(task, map_number)[0]
        
    else:
        raw_game_map_data, currentTask = game_map.getGameMap(task, map_number)

    # Change the raw map of string into a list of lists
    game_map_data = raw_game_map_data.split("\n")
    for row in range(len(game_map_data)):
        game_map_data[row] = list(game_map_data[row])

    # Set the size of the map
    game_map_total_rows = len(game_map_data)
    game_map_total_cols = len(game_map_data[0])

    a_block_width  = total_width  / (game_map_total_cols+2)
    a_block_height = total_height / (game_map_total_rows+2)

    # Search for the initial position of the robot
    for row in range(game_map_total_rows):
        for col in range(game_map_total_cols):
            if game_map_data[row][col] == "P":
                robot_row = row
                robot_col = col


# This function returns True if the robot can move to the target location
# or False otherwise
def isMoveable(target_row, target_col):
    # The robot moves out of the game map area
    if target_row < 0 or target_row >= game_map_total_rows or \
       target_col < 0 or target_col >= game_map_total_cols:
        print("The robot is out of bounds!")
        return False

    # A wall is there
    if game_map_data[target_row][target_col] == "B":
        print("The robot hits the wall!")
        return False

    return True


def handledDefDrawingTurtles():
    for row in range(game_map_total_rows):
        row_turtles = []
        for col in range(game_map_total_cols):
            newTurtle = turtle.Turtle()
            newTurtle.up()
            newTurtle.goto((col+1) * a_block_width, (row+1)*a_block_height)
            newTurtle.speed(0)
            newTurtle.hideturtle()
            row_turtles.append(newTurtle)
        drawing_turtles.append(row_turtles)

    for row in range(game_map_total_rows):
        row_turtles = []
        for col in range(game_map_total_cols):
            newTurtle = turtle.Turtle()
            newTurtle.up()
            newTurtle.goto((col+1) * a_block_width, (row+1)*a_block_height)
            newTurtle.speed(0)
            newTurtle.hideturtle()
            row_turtles.append(newTurtle)
        layer2_drawing_turtles.append(row_turtles)

def handleHistoryPath(row, col):
    # To improve the speed, put the path drawing here
    if game_map_data[row][col]    == "Ea":
        writeBlock(row, col, ">")
    elif game_map_data[row][col]  == "We":
        writeBlock(row, col, "<")
    elif game_map_data[row][col]  == "No":
        writeBlock(row, col, "^")
    elif game_map_data[row][col]  == "So":
        writeBlock(row, col, "v")
    # To improve the speed, put the path drawing here

# This function tries to move the robot to a new location
def move(target_row, target_col, sign):
    global robot_row, robot_col

    if isMoveable(target_row, target_col):
        # Change the current block to 'history'
        #game_map_data[robot_row][robot_col] = "H"
        game_map_data[robot_row][robot_col] = sign

        handleHistoryPath(robot_row, robot_col)

        # Move the robot to the new location
        robot_row = target_row
        robot_col = target_col


        # Change the block to P if the robot is not at the exit
        if game_map_data[robot_row][robot_col]  != "E":
            game_map_data[robot_row][robot_col]  = "P"

# This function tries to move the robot to the north
def moveNorth():
    if not startToMove:
        return
    move(robot_row - 1, robot_col, "No")
    robot_turtle.shape("robot_north.gif")


# This function tries to move the robot to the south
def moveSouth():
    if not startToMove:
        return
    move(robot_row + 1, robot_col, "So")
    robot_turtle.shape("robot_south.gif")

# This function tries to move the robot to the east
def moveEast():
    if not startToMove:
        return
    move(robot_row, robot_col + 1, "Ea")
    robot_turtle.shape("robot_east.gif")

# This function tries to move the robot to the west
def moveWest():
    if not startToMove:
        return
    move(robot_row, robot_col - 1, "We")
    robot_turtle.shape("robot_west.gif")



# This function moves the robot based on the given decision
# The decision can be one of "NORTH", "SOUTH", "EAST" and "WEST" 
def moveRobot(decision):
    global is_finished, forceUpdate

    # Show the decision
    print(decision)

    # Move the robot based on the decision
    if decision == "NORTH":
        moveNorth()
    elif decision == "SOUTH":
        moveSouth()
    elif decision == "EAST":
        moveEast()
    elif decision == "WEST":
        moveWest()
    elif decision == "NONE":
        pass
    else:
        print("ERROR IN COMMAND, cannot understand the command:"+str(decision))
        return

    if game_map_data[robot_row][robot_col] == "E":
        is_finished = True
        forceUpdate = True
        global robot_view
        robot_view = False

    # Update the game map
    drawGameMap()
    
    # Show the game over message when the game finishes
    if is_finished:
        showGameOver()

def clearBlock(row,col):
    drawing_turtles[row][col].clear()

def clearBlock2(row,col):
    layer2_drawing_turtles[row][col].clear()

# This function is used for drawing a block (wall or empty space) in the map
def drawBlock(row, col, pencolor, fillcolor):
    # Make sure the tracer is not on
    turtle.tracer(False)
    
    # Clear the original block
    clearBlock(row, col)
    # Set up the color
    drawing_turtles[row][col].pencolor(pencolor)
    drawing_turtles[row][col].fillcolor(fillcolor)

    # Draw the block
    drawing_turtles[row][col].down()
    drawing_turtles[row][col].begin_fill()
    drawing_turtles[row][col].setheading(0)
    for _ in range(2):
        drawing_turtles[row][col].forward(a_block_width)
        drawing_turtles[row][col].left(90)
        drawing_turtles[row][col].forward(a_block_height)
        drawing_turtles[row][col].left(90)
    drawing_turtles[row][col].end_fill()
    drawing_turtles[row][col].up()

# This function is used for drawing a block (wall or empty space) in the map
def drawBlockL2(row, col, pencolor, fillcolor):
    # Make sure the tracer is not on
    turtle.tracer(False)
    # Clear the original block
    clearBlock2(row, col)
    # Set up the color
    layer2_drawing_turtles[row][col].pencolor(pencolor)
    layer2_drawing_turtles[row][col].fillcolor(fillcolor)

    # Draw the block
    layer2_drawing_turtles[row][col].down()
    layer2_drawing_turtles[row][col].begin_fill()
    layer2_drawing_turtles[row][col].setheading(0)
    for _ in range(2):
        layer2_drawing_turtles[row][col].forward(a_block_width)
        layer2_drawing_turtles[row][col].left(90)
        layer2_drawing_turtles[row][col].forward(a_block_height)
        layer2_drawing_turtles[row][col].left(90)
    layer2_drawing_turtles[row][col].end_fill()
    layer2_drawing_turtles[row][col].up()

writing_turtle = None

# This function is used for drawing a block (wall or empty space) in the map
def writeBlock(row, col, text):
    # Make sure the tracer is not on
    turtle.tracer(False)

    # Clear the original block
    clearBlock(row, col)

    # Go to the starting position
    drawing_turtles[row][col].hideturtle()
    drawing_turtles[row][col].up()
    drawing_turtles[row][col].goto((col+1+0.5) * a_block_width, (row+1+1)*a_block_height)

    # Draw the arrow
    drawing_turtles[row][col].write(str(text),
        align="center", font=("Arial", int(a_block_height/2), "bold"))    

    drawing_turtles[row][col].goto((col+1) * a_block_width, (row+1)*a_block_height)

def handleRobotAppearance():
    # When the game is not over
    if not is_finished:
        drawBlock(robot_row, robot_col, "brown", "")
        robot_turtle.up()
        robot_turtle.goto((robot_col+1+0.5) * a_block_width, (robot_row+1+0.5)*a_block_height)

draw_init = False
# This function draws the game map inside the turtle window
def drawGameMap():
    global draw_init, forceUpdate

    # Disable the tracer
    turtle.tracer(False)

    # If the game is initialized...
    if not draw_init or is_finished:
        # Draw the game blocks
        for row in range(len(game_map_data)):
            for col in range(len(game_map_data[0])):
                # If the robot cannot view the rest of the map
                if robot_view and not is_finished and \
                    abs(robot_row - row) + abs(robot_col - col) > 1:
                        # drawBlock(row, col, "", "black")
                        drawBlockL2(row, col, "", "black")
                        continue

                # If it is a block...
                elif game_map_data[row][col] == "B":
                    if not is_finished:
                        drawBlock(row, col, "", "blue")
                    else:
                        drawBlock(row, col, "", (150, 150, 255))

                # If it is the exit...
                elif game_map_data[row][col] == "E":
                    if not is_finished:
                        drawBlock(row, col, "", "red")
                    else:
                        drawBlock(row, col, "", (255, 150, 150))
                elif not is_finished:
                    if game_map_data[row][col] == " ":
                        clearBlock(row,col)
                    else:
                        if not robot_view:
                            handleHistoryPath(row, col)

        # We only do the initialization once
        draw_init = True

    if forceUpdate:
        for row in range(len(game_map_data)):
            for col in range(len(game_map_data[0])):
                # If the robot cannot view the rest of the map
                if robot_view and not is_finished:
                    drawBlockL2(row, col, "", "black")
                    continue
                else:
                    clearBlock2(row, col)

        forceUpdate = False

    if robot_view:
        for row in range(len(game_map_data)):
            if abs(robot_row - row) > 2:
                continue
            for col in range(len(game_map_data[0])):
                if abs(robot_col - col) > 2:
                    continue
                # If the robot cannot view the rest of the map
                if robot_view:
                    if robot_view and not is_finished and \
                        abs(robot_row - row) + abs(robot_col - col) > 1:
                            # drawBlock(row, col, "", "black")
                            drawBlockL2(row, col, "", "black")
                            continue
                    else:
                        clearBlock2(row, col)
                else:
                    clearBlock2(row, col)

        forceUpdate = False

    # Draw the robot
    handleRobotAppearance()

    # Update the turtle window
    turtle.tracer(True)


# This function shows the game over message inside the turtle window
# when the game is over
def showGameOver():
    # Disable the tracer
    turtle.tracer(False)

    # Draw the game over text
    robot_turtle.hideturtle()
    drawing_turtle.goto(75, 100)
    drawing_turtle.setheading(0)
    thickness = drawing_turtle.width()
    drawing_turtle.width(3)
    drawing_turtle.color("red", "white")
    drawing_turtle.down()
    drawing_turtle.begin_fill()
    drawing_turtle.goto(425, 100)
    drawing_turtle.goto(425, 160)
    drawing_turtle.goto(75, 160)
    drawing_turtle.goto(75, 100)
    drawing_turtle.end_fill()
    drawing_turtle.up()
    drawing_turtle.width(thickness)
    
    drawing_turtle.goto(250, 150)
    drawing_turtle.color("magenta")
    drawing_turtle.write("You finished the game!", \
        align="center", font=("Comic Sans", 20, "bold"))

    # Update the turtle window
    turtle.tracer(True)

# This function is used by the key event to toggle the robot view
def toggleRobotView():
    global robot_view, forceUpdate
    robot_view = not robot_view
    forceUpdate = True

startToMove = False

# The function sets the decision making functions
def assignDecisionFuncForTask0(func):
    global task_handlers
    task_handlers["task0"] = func

def assignDecisionFuncForTask1(func):
    global task_handlers
    task_handlers["task1"] = func

def assignDecisionFuncForTask2(func):
    global task_handlers
    task_handlers["task2"] = func
    
def assignDecisionFuncForTask3(func):
    global task_handlers
    task_handlers["task3"] = func
    
def assignDecisionFuncForTask4(func):
    global task_handlers
    task_handlers["task4"] = func

# This is the main game loop
def gameLoop():
    global robot_col, robot_row, startToMove, currentTask
    # Give up if no function is given
    if current_task_handler == None:
        return

    startToMove = False
    before_col, before_row = robot_col, robot_row
    before_currentTask = currentTask
    
    # Get the decision of the robot
    decision = current_task_handler()

    robot_col, robot_row = before_col, before_row
    currentTask = before_currentTask
    # Make the robot move based on the decision
    startToMove = True
    moveRobot(decision)

    # Repeat the game loop
    if not is_finished:
        turtle.ontimer(gameLoop, timing) # turtle.ontimer() is not taught this semester


# This function sets up the entire robot game using the selected game map
# and then starts the game
def startGame():
    global robot_turtle, drawing_turtle, writing_turtle
    global current_task_handler

    # Set up the turtle window
    turtle.setup(500, 500)
    turtle.title("COMP1021 Robot Game")

    # Set up the coordinate system of the window to be the same as the map
    #turtle.setworldcoordinates(-1, game_map_total_rows + 0.5, game_map_total_cols + 0.5, -1)
    turtle.setworldcoordinates(0, 500, 500, 0)

    turtle.tracer(False)
    # Add the robot images as turtle shapes
    turtle.addshape("robot_north.gif")
    turtle.addshape("robot_south.gif")
    turtle.addshape("robot_east.gif")
    turtle.addshape("robot_west.gif")

    # Create a robot turtle
    robot_turtle = turtle.Turtle()
    robot_turtle.up()
    robot_turtle.shape("robot_north.gif")

    # Create a turtle for drawing the game graphics such as the map
    drawing_turtle = turtle.Turtle()
    drawing_turtle.up()
    drawing_turtle.hideturtle()
    
    handledDefDrawingTurtles()

    # Create a turtle for writing the game text such as the map
    writing_turtle = turtle.Turtle()
    writing_turtle.up()
    writing_turtle.hideturtle()

    # Set up the key event for the 'r' key
    turtle.onkeypress(toggleRobotView, 'r')
    turtle.listen()

    # Update the game map
    drawGameMap()

    # Select corresponding task handler
    if currentTask == "task0":
        current_task_handler = task_handlers["task0"]

    elif currentTask == "task1":
        current_task_handler = task_handlers["task1"]
        
    elif currentTask == "task2":
        current_task_handler = task_handlers["task2"]

    elif currentTask == "task3":
        current_task_handler = task_handlers["task3"]

    elif currentTask == "task4":
        current_task_handler = task_handlers["task4"]
    
    # Start the game loop
    turtle.ontimer(gameLoop, timing) # turtle.ontimer() is not taught this semester
    
    turtle.done()
