"""
This example shows the use of advanced operators **, // and -.
"""

# Using the power operator **
print(2 ** 2)
print(3 ** 2)

# Using the integer division operator //
print(3 / 3, 3 // 3)
print(4 / 3, 4 // 3)
print(5 / 3, 5 // 3)
print(6 / 3, 6 // 3)
print(7 / 3, 7 // 3)
print(8 / 3, 8 // 3)

# Using the negation operator -
x = 10
print(-x)

"""
This example shows that you can use a shortcut to write an equal sign with
some arithmetic operators when you put the result back to the same varible.
"""

calorie = 3500
calorie += 800      # i.e. calorie = calorie + 800
print(calorie)

pigs = 6
pigs *= 5           # i.e. pigs = pigs * 5
print(pigs)

cakes, students = 40, 8
cakes /= students   # i.e. cakes = cakes / students
print(cakes)

marks = 100
marks -= 20         # i.e. marks = marks - 20
print(marks)

hello = "Hello"
hello += "!"        # i.e. hello = hello + "!"
print(hello)

hello = "Hello"
hello *= 5        # i.e. hello = hello * 5
print(hello)

if "shark" in "baby shark dance":
    print("Yes")

if "shark" not in "baby shark dance":
    print("Yes")

"""

- Highest precedence -
( )
**
-x, +x
*
, /, %, //
+, - <, >, <=, >=, !=, ==
in, not in
logical not
logical and
logical or
- Lowest precedence -
"""
