# Python Commands
This is the list of commands which I know in Python language

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