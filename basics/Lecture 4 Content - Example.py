import turtle
print('Beautiful Modern Art!')
print()
print('This program will display some beautiful')
print('modern art, according to your choices!')
print()
print('Please choose one of the follwoing')
print()
print('1 - using squares/rectangles')
print('2 - using turtle.circle')
print()

choice = int(input("Which one do you want?"))

import turtle

if choice == 1:
    print('Please choose one of the following')
    print()
    print('a - simple art with squares/rectangles')
    print('b - advanced art with squares/rectangles')
    print()
    second_choice = input('Which one do you want?')
    if second_choice == 'a':
        turtle.color("red", "blue")
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.hideturtle()
    elif second_choice == 'b':
        turtle.color("red", "blue")
        turtle.begin_fill()
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.hideturtle()
        turtle.end_fill()
    else:
        print('You need to enter a or b')

elif choice == 2:
    print('Please choose one of the following')
    print()
    print('a - simple art with circle.turtle')
    print('b - advanced art with circle.turtle')
    print()
    second_choice = input('Which one do you want?')
    if second_choice == 'a':
        turtle.color("red", "blue")
        turtle.circle(200)
    elif second_choice == 'b':
        turtle.color("red", "blue")
        turtle.begin_fill()
        turtle.circle(200)
        turtle.end_fill()
    else:
        print('You need to enter a or b')
else:
    print('You need to enter 1 or 2!')
