import turtle
import random
print(list(range(1,6)))  #print as a list
colors = ["blue", "green", "red"]
y = 0
while y <4:
    x = 0
    while x < 4:
        print(y,x)
        turtle.color(random.choice(colors))
        turtle.up()
        turtle.goto(x*100,y*100)
        turtle.dot(100)
        x = x+1
    y = y+1

for mubin in range(20):
    print(mubin, mubin*mubin)

for hasan in range(2, 5): #loops for about 3 times // 5-2 = 3
    print(hasan, hasan*hasan)

for m in range(200, 300, 5):   #loops on every 5 interval
    print(m)

for h in range(100):  #does not output in new lines
    print(h, end = " ")
for s in range(10): #printing some text in between every loop
    print(s, end = " then ")

for c in colors:
    print(c)

#Drawing a start shape
#for _ in range(5):
    #turtle.forward(200)
    #turtle.right(144)

#Drawing a spiral pattern 1
#for i in range(0, 500, 5):
    #turtle.forward(i)
    #turtle.right(91)

#Drawing Spiral Pattern II
#for i in range(0, 400, 2):
    #turtle.forward(i)
    #turtle.right(89)

#for i in range(401, 0, -2):
    #turtle.forward(i)
    #turtle.right(89)

#Drawing a Flower created by hexagons
#for i in range(10):
    #for i in range(6):
        #turtle.forward(120)
        #turtle.right(60)
    #turtle.right(36)

#Drawing rows of dots
#size = 20
#turtle.color("brown")
#turtle.up()
#turtle.hideturtle()
#for i in range(0,15, 2):
    #for j in range(i+1):
        #turtle.dot(size)
        #turtle.forward(size)
    #turtle.backward(size*(i+2))
    #turtle.right(90)
    #turtle.forward(size)
    #turtle.left(90)
#turtle.down()
#turtle.showturtle()
