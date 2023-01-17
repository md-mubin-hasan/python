import turtle
turtle.tracer(False)
for i in range(0,400,2): #200 iterations
    turtle.forward(i)
    turtle.right(89)

for i in range(401,0,-2): #How many will it draw?
    turtle.forward(i)
    turtle.right(89)

turtle.tracer(True)

print(len(range(589,11,-2)))


for i in range(589,11,-2):
    print(i, end=" ")
