# Python Commands
This is the list of commands which I know in Python language

## Variables & Data Types

> Storing multiple data in one line
```
a, b, c = 12, 13, 14
d = e = f = 15
```
We can use single quotes inside a string written with double quotes, and vice versa.
```
text1 = "I thought to myself 'This changes everything'"
text2 = 'I thought to myself "This changes everything"'
```
To use a double quote within a string written with double quotes, *escape* the inner quotes by prefixing them with the `\` character.

```
text3 = "I thought to myself \"This changes everything\""
text4 = 'I thought to myself \'This changes everything\''
```

Strings created using single or double quotes must begin and end on the same line. To create multiline strings, use three single quotes `'''` or three double quotes `"""` to begin and end the string. Line breaks are represented using the newline character `\n`.

```
text5 = """I thought to myself
This changes everything"""
```

```
type(10/3)   //float
type(10/2)   //float
type(10//2)  //int
```

> Booleans are automatically converted to `int` when used in arithmetic operations. `True` are converted to `1` and `False` are converted to `0`.

Only the following values are evaluated as `False`, (*falsy* values):
* The `False` itself
* The integer `0`
* The float `0.0`
* The empty value `None`
* The empty text `""`
* The empty list `[]`
* The empty tuple `()`
* The empty dictionary `{}`
* The empty set `set()`
* The empty range `range(0)`

Any value in `Python` can be converted to a boolean using `bool()` function

```
text6 = bool(range(10))  //True is stored in text6
```
## Lambda Function

```
def cube(y):
    return y*y*y

lambda_cube = lambda y: y*y*y
print(cube(5))
print(lambda_cube(5))
```

## Ternary Operators
```
a,b = 1, 2
print("a" if a>b else "b")
```
[on_true] if [expression] else [on_false]  

```
import random
a, b = random.randint(2,10), random.randint(0,10)
result1 = "a" if a>b else "b"
print(result)
```
([on_false], [on_true]) [expression]  //Using tuples
```
result2 = (b,a) [a>b]
result3 = (f"b:{b}", f"a:{a}")[a>b]
```
{True:[on_true],False:[on_false]}[expression]  //Using dictionaries
```
result3 = {True:f"b:{b}",False:f"a:{a}"}[a<b]
print(result3)
result4 = {False:f"b:{b}",True:f"a:{a}"}[a<b]
print(result4)
```
(lambda: [on_true], lambda: [on_false])[expression]()   //Using lambda function
```
result5 = (lambda: f"a:{a}", lambda: f"b:{b}")[a>b]()
print(result5)
```
## Nested Ternary Operator
```
result6 = "Less than or equal to zero" if a<=0 else "Between 0 and 3" if a>0 and a<3 else "Greater than 2"
print(result6)
```