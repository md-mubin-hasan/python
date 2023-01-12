# Python Commands
This is the list of commands which I know in Python language


## Help

```
help(variable_name.methodname)
```
> Jupyter Notebook / Jupyterlab

```
?variable_name.methodname
```
To find the execution time
```
%%time
```
To see what a particular function does, we can press SHIFT+Tab and check

## Distinction between *statement* and *expression* in **Python**

> **Statements:** A statement is an instruction that can be executed. Every line of code we have written so far is a statement e.g. assigning a variable, calling a function, conditional statements using `if`, `else`, and `elif`, loops using `for` and `while` etc.

> **Expressions:** An expression is some code that evaluates to a value. Examples include values of different data types, arithmetic expressions, conditions, variables, function calls, conditional expressions, etc.

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
type(10/3)   # float
type(10/2)   # float
type(10//2)  # int
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
text6 = bool(range(10))  # True is stored in text6
```

> The None type includes a single value `None`, used to indicate the absence of a value. `None` has the type `NoneType`. It is often used to declare a variable whose value may be assigned later

```
nothing = None
text7 = type(nothing) # stores "NoneType" in text7
```

> String
```
multiline_string = """a
b"""
text8 = list(multiline_string)   # stores ['a','\n','b']
```

> **Methods**: Methods are functions associated with data types and are accessed using the `.` notation e.g. `variable_name.method()` or `"a string".method()`. Methods are a powerful technique for associating common operations with values of specific data types.

```
cost_of_ice_bag = 1.25
profit_margin = .2
number_of_bags = 500
text9 = """If a grocery store sells ice bags at $ {} per bag, with a profit margin of {} %, 
then the total profit it makes by selling {} ice bags is $ {}."""

text10 = text9.lower()
text10 = text9.upper()
text10 = text9.capitalize() # changes the first character to uppercase
text10 = text9.replace("sample1", "sample2")   # sample1 will be replaced by sample2, it only returns the value once, it does not change the orignal text fully
text10 = text9.split("anysymbol") # this outputs a list
text10 = text9.strip()  # removes whitespace in the beginning and ending of the string 
text10 = text9.format(parameter1, parameter2, ...) # See the example below, placeholder `{}` in text9 is neccessary

text10 = text9.format(cost_of_ice_bag, profit_margin*100, number_of_bags, total_profit)
print(text10)

print("""If a grocery store sells ice bags at $ {} per bag, with a profit margin of {} %, 
then the total profit it makes by selling {} ice bags is $ {}.""".format(cost_of_ice_bag, profit_margin*100, number_of_bags, total_profit))
print('This is a value {:.0f}'.format(32.3456))         # 32
print('This is a value {:.1f}'.format(32.3456))         # 32.3
```

> List

```
list1 = ['a','b','c','d']
text11 = list1.pop(3)  # text11 stores 'd' but deletes the value from list1

list2 = list1.copy()  # Changing the content of list2 will not affect the content of list1
```

> Tuple

```
single_element_tuple1 = 4,      # it stores as (4,)
single_element_tuple1 = (3,)
not_tuple = (4)                 # it stores as 4
a_tuple = 34, True, None, "Mubin", 23.3, "Moriom"

point = (3,4)
point_x, point_y = point        # point_x = 3 and point_y = 4

# Converting a list into a tuple and vice verse, use tuple() and list() respectively
```

> Dictionaries

```
# Dictionaries can also be created using dict function

person1 = dict( name = 'Mubin', gender = 'male', age = 20, married = False)
print(person1)          #  outputs {'name' : 'Mubin', 'gender' : 'male', 'age' : 20, 'married' : False}

# We can use get method to access the value associated with a key
text = person1.get('name')
```
To remove a key and associated value from a dictionary, use the `pop` method
```
text = person1.pop('age')   # stores the value associated with the key 'age'
```

```
list1 = person1.keys()      # it stores dict_keys(['name', 'gender', 'age', 'married'])
list2 = person1.values()    # it stores dict_values(['Mubin', 'male', 20, False])
list3 = person1.items()     # it stores dict_items([('name', 'Mubin'), ('gender', 'male'), ('age', 20), ('married', False)])

list1 = list(list1)         # now we can access the values from list1 treating it as a list, like list1[0] outputs 'name'
```

> Pass Statement

```
if num % 2 == 0:
    pass                        # it does nothing
elif num % 3 == 0:
    print("Divisible by 3")
```

> Enumerate function

```
a_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for i in range(len(a_list)):
    print('The value at position {} is {}.'.format(i, a_list[i]))

for i, val in enumerate(a_list):
    print('The value at position {} is {}.'.format(i, val))
```

> Pair

```
for x, y in zip(x_cordinate, y_coordinate):
    result += x^2 + y^2
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
([on_false], [on_true]) [expression]  # Using tuples
```
result2 = (b,a) [a>b]
result3 = (f"b:{b}", f"a:{a}")[a>b]
```
{True:[on_true],False:[on_false]}[expression]  # Using dictionaries
```
result3 = {True:f"b:{b}",False:f"a:{a}"}[a<b]
print(result3)
result4 = {False:f"b:{b}",True:f"a:{a}"}[a<b]
print(result4)
```
(lambda: [on_true], lambda: [on_false])[expression]()   # Using lambda function
```
result5 = (lambda: f"a:{a}", lambda: f"b:{b}")[a>b]()
print(result5)
```
## Nested Ternary Operator
```
result6 = "Less than or equal to zero" if a<=0 else "Between 0 and 3" if a>0 and a<3 else "Greater than 2"
print(result6)
```

## Exception Handling
```
try:
    print(x)
except:
    print("An exception occurred")
```

> NameError
```
try:
    print(x)
except NameError:
    print("Variable is not defined")
except:
    print("Something else went wrong!")
```

> `else` keyword is used to define a block of code to be executed if no errors were raised
```
try:
    print("Hello!")
except:
    print("Something went wrong!")
else:
    print("Nothing went wrong!")
```

> `finally` keyword is used to define a block of code to be executed regardless if the `try` block raises an error or not
```
try:
    print(x)
except:
    print("Something went wrong!")
finally:
    print("The try-except is finished!")
```

> An example of trying to open and write an file that is not writable

```
try:
    f = open("demofile.txt")
    try:
        f.write("Moriomubin")
    except:
        print("Something went wrong when writing to the file!")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
```

> `is` keyword is used to test whether two variables belong to the same object. The test will return `True` if the two objects are same else it will return `False` even if the two objects are 100% equal. Note: the `==` operator is used to test if the two objects are same.

```
a = 10
b = 10

if a is b:
    print(True)
else:
    print(False)

# Prints True

x = 'Mubin'
y = 'Mubin'

if x is y:
    print(True)
else:
    print(False)

# Prints True

ab = ['a', 'b', 'c']
ac = ['a', 'b', 'c']

if ab is ac:
    print(True)
else:
    print(False)

# Prints False

print(ab is ac) # outputs False
print(ab == ac) # outputs True
```

> Raising an exception

```
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero!")

y = 'hello'

if not type(y) is int:
    raise TypeError("Only integers are allowed!")
```

## Functions

> **Named Arguments:** Python allows to enter named arguments when calling a function
```
def emi_calculate(amount, duration):
    return amount/duration

loan_calculate(amount = 12000, duration = 12)
```
## Documenting functions using Docstrings

> A docstring describes what the function does, and provide some explanations about the arguments. It is used by the `help` function.

```
def loan_emi(amount, duration, rate, down_payment=0):
    """Calculates the equal montly installment (EMI) for a loan.
    
    Arguments:
        amount - Total amount to be spent (loan + down payment)
        duration - Duration of the loan (in months)
        rate - Rate of interest (monthly)
        down_payment (optional) - Optional intial payment (deducted from amount)
    """
    loan_amount = amount - down_payment
    try:
        emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount / duration
    emi = math.ceil(emi)
    return emi

help(loan_emi)
# Outputs the docstring
```

## Modules

```
import math
a = math.ceil(1.2)
```

```
from math import ceil
a = ceil(1.2)
```
## OS and Filesystem

```
import os

os.cwd()            # Checking current present directory
os.listdir()        # Checking the list of files in a directory
os.listdir('.')     # checking the relative path

os.makedirs('./foldername', exist_ok = True)         # Creating a new directory in the present directory. If exist_ok is False (the default), a FileExistsError is raised if the target directory already exists.
a = 'foldername' in os.listdir('.')                 # Stores True if the folder name is present in the present directory
b = os.listdir('./foldername')                      # Absolute path, list of files inside a directory of present directory. If that directory is empty, empty list is stored in b

```
> Reading from a file 

```
file1 = open('filename.filetype', mode = 'r')       # Filename can have absolute path starting with './', there are different modes, check those with help function
file1_contents = file1.read()
print(file1_contents)
file1.close()                   # After closing the file, file1.read() will not work
```

> Closing files automatically using `with`

```
with open('./demofolder/filename.txt', mode = 'r') as file2:
    file2_contents = file2.read()
    print(file2_contents)
```

> Reading a file line by line

```
with open('./demofolder/filename.txt', mode = 'r') as file2:
    file2_contents = file2.readlines()                              # Each line is stored as an element of a list
    print(file2_contents)
```

> Processing data from files

```
def parse_headers(header_line):
    return header_line.strip().split(',')

def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            try:
                values.append(float(item))
            except ValueError:
                values.append(item)
    return values

def create_item_dict(values, headers):
    result = {}
    for value, header in zip(values, headers):
        result[header] = value
    return result

def read_csv(path):
    result = []
    
    # Open the file in read mode
    with open(path, 'r') as f:
        # Get a list of lines
        lines = f.readlines()
        
        # Parse the header
        headers = parse_headers(lines[0])
        
        # Loop over the remaining lines
        for data_line in lines[1:]:
            # Parse the values
            values = parse_values(data_line)
            
            # Create a dictionary using values & headers
            item_dict = create_item_dict(values, headers)
            
            # Add the dictionary to the result
            result.append(item_dict)
    return result

def write_csv(items, path):

    # Open the file in write mode
    with open(path, 'w') as f:
    
        # Return if there's nothing to write
        if len(items) == 0:
            return
        
        # Write the headers in the first line
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')
        
        # Write one item per line
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(','.join(values) + "\n")
```

```
with open('./data/emis2.txt', 'w') as f:
    for loan in loans2:
        f.write('{},{},{},{},{}\n'.format(
            loan['amount'], 
            loan['duration'], 
            loan['rate'], 
            loan['down_payment'], 
            loan['emi']))
```
## NumPy

> To install numpy 
```
!pip install numpy --upgrade --quiet
```

> Array

```
import numpy as np
a = np.array([23,32,22,33])
b = np.array([.4,.5,.6,.7])

ab = a*b
ab_dot = np.dot(a,b)  # Dot product of the arrays a and b
ab_sum = ab.sum()     # Same as ab_sum = (a*b).sum()

type(a)     # numpy.ndarray
a.shape     # (4,)
a.dtype     # dtype('int32')

aa = np.array([
                [12, 13, 14, 15],
                [23, 24, 25, 26],
                [34, 35, 36, 37],
                [45, 46, 47, 48]
                ])
aa.shape    # (4,4) == (outer dimension, inner dimension)  

aaa_matrixmul1 = np.matmul(aa, a)
aaa_matrixmul2 = aa @ a
```
> Urllib.request Module

```
import urllib.request

urllib.request.urlretrieve(
    'https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 
    'climate.txt')
```

```
from urllib.request import urlretrieve

urlretrieve('https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 'climate.txt')

# urlretrieve('https://sample.url', './demofolder/climate.txt')
```
> Converting txt into array

```
data = np.genfromtxt('filename.txt', delimiter = ',', skip_header = 1)
```

> Writing txt into a file

```
np.savetxt('filename.txt', variable_name, fmt = '%.2f', delimiter = ',', header = 'header1, header2, header3', comments = '')
```

> Reshaping the array

```
a_reshaped1 = a.reshape(2, 2)
a_reshaped2 = a.reshape(4, 1)   # (outer dimension, inner dimension) == (row, column)
```

> Concatenate function

```
a = np.array([[1,2],[3,4]])     #(2, 2)
b = np.array([[5,6]])           #(1, 2)

concated1 = np.concatenate((a,b), axis = 0)     #a and b has to be same dimensional array
concated2 = np.concatenate((a,b.T), axis = 1)   #np.concatenate((a, b.reshape(2,1)), axis = 1)
concated3 = np.concatenate((a,b), axis = None)  #a and b does not need to be in same dimension
```

> Mathematics: `np.sum`, `np.exp`, `np.round`, arithemtic operators

> Array manipulation: `np.reshape`, `np.stack`, `np.concatenate`, `np.split`

> Linear Algebra: `np.matmul`, `np.dot`, `np.transpose`, `np.eigvals`

> Statistics: `np.mean`, `np.median`, `np.std`, `np.max`

> NumPy Documentation : [numpy](https://numpy.org/doc/stable/reference/routines.html)

> Forming arrays

```
# Range with start, end and step
a1 = np.arange(5)           # array([0, 1, 2, 3, 4])
a2 = np.arange(3, 20)       # array([ 3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
a2 = np.arange(3, 20, 4)    # array([ 3,  7, 11, 15, 19])

b1 = np.ones(4)             # array([1., 1., 1., 1.])
b2 = np.ones((4,))          # array([1., 1., 1., 1.])
b3 = np.ones((3,3))         # array([[1., 1., 1.],[1., 1., 1.],[1., 1., 1.]])
b4 = np.ones([2, 2, 3])     # array([[[1., 1., 1.],[1., 1., 1.]],[[1., 1., 1.],[1., 1., 1.]]])

c1 = np.zeros(4)            # array([0., 0., 0., 0.])
c2 = np.zeros((4,))         # array([0., 0., 0., 0.])
c3 = np.zeros((4,2))        # array([[0., 0.],[0., 0.],[0., 0.],[0., 0.]])
c4 = np.zeros([2,2,3])      # array([[[0., 0., 0.],[0., 0., 0.]],[[0., 0., 0.],[0., 0., 0.]]])

# Identity Matrix
d = np.eye(3)               # array([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]])

# Random Vector forms from uniform distribution [0,1)
e1 = np.random.rand(4)          # array([0.67720034, 0.78128189, 0.9746822 , 0.66433952])
# Random matrix
e2 = np.random.rand(2,3)        # array([[0.21728667, 0.87190509, 0.89748379],[0.47179849, 0.83554905, 0.86015455]])

f1 = np.random.randn(4)         # standard normal distribution (includes negative numbers) # array([-0.46426101,  0.36486801,  1.03339286,  1.29384229])
f2 = np.random.randn(2,3)       # array([[ 1.33146919, -1.95268722,  1.55484275],[ 0.71057842, -0.46610497,  1.37420616]])

# a n-dimensional array with a specific number
g1 = np.full([2,3], 20)
g2 = np.full([2, 3, 4], 21)
g3 = np.full([2,3,4,5], 22)

# Equally spaced numbers in a range
h1 = np.linspace(3, 18, 7)      # array([ 3. ,  5.5,  8. , 10.5, 13. , 15.5, 18. ])
```

> Scaling

a1 + 2         # Adds 2 to each element of the the array a1
a1 - 2         # Subtracts 2 from each element of the array a1
a1 % 2         # Find the modulus from each element of the array a1
a1 / 2         # Division by scalar
a1 * a2        # Element-wise multiplication

> Broadcasting

Broadcasting only works if one of the arrays can be replicated to match the array's shape.

```
a = np.arange(3) + 5                # a = array([5, 6, 7]) which is array([0, 1, 2]) + array([5, 5, 5])
a = array([0,1,2]) + 5
b = np.ones((3,3)) + np.arange(3)     # b = array([[1,2,3],[1,2,3],[1,2,3]]) which is array([[1,1,1],[1,1,1],[1,1,1]]) + array([[0,1,2],[0,1,2],[0,1,2]])
b = array([[1,1,1],[1,1,1],[1,1,1]]) + array([0,1,2])
c = np.arange(3).reshape(3,1) + np.arange(3)    # c = array([[0,1,2],[1,2,3],[2,3,4]]) which is array([[0,0,0],[1,1,1],[2,2,2]]) + array([[0,1,2],[0,1,2],[0,1,2]])
c = array([[0],[1],[2]]) + array([0,1,2])
```

> Array Comparison 

```
arr1 = np.array([[1, 2, 3],[3, 4, 5]])
arr2 = np.array([[2, 2, 3],[1, 2, 5]])

mb = arr1 == arr2           # mb = array([[False, True, True],[False, False, True]])  same rule applies to other comparison operators such as !=, >, >=, <, <=
ms = (arr1 == arr2).sum()
```

> Array Indexing & Slicing

```
arr3 = np.array(
   [[[11, 12, 13, 14], 
     [13, 14, 15, 19]],     
    [[15, 16, 17, 21], 
     [63, 92, 36, 18]], 
    [[98, 32, 81, 23],      
     [17, 18, 19.5, 43]]])
arr3.shape      # (3, 2, 4)

a = arr3[0]             # a = array([[11., 12., 13., 14.],[13., 14., 15., 19.]])
b = arr3[0][0]          # b = array([11., 12., 13., 14.]) same as arr3[0, 0]
c = arr3[0][0][0]       # c = 11.0 same as arr3[0,0,0]

# Subarray using ranges
aa = arr3[1:, :1, :3]       # aa = array([[[15,16,17]],[[98,32,81]]])
aa.shape                    # (2,1,3)

# Mixing indices and ranges
ab = arr3[1:, 0, :3]        # ab = array([[15,16,17]],[[98,32,81]])
ab.shape                    # (2,3)
ac = arr3[1:, 0, 0]         # ac = array([15, 98])
ac.shape                    # (2,)
```

## Pandas

To install Panda module

```
!pip install pandas --upgrade --quiet
```

> Initial code

```
import panda as pd

covid_df = pd.read_csv('filename.csv')

type(covid_df)          # Data type is DataFrame, full form is pandas.core.frame.DataFrame
print(covid_df)         # The data is printed as a table, together with indexing
covid_df.info()         # Summary of the data is returned, (Data type, Column Header, Number of Rows and many more)
covid_df.describe()     # Statistical information for numerical columns (mean, standard deviation, minimum/maximum values, and the number of non-empty values)
covid_df.columns        # Get the list of column names
covid_df.shape          # Get the number of rows & columns as a tuple
```

> Retrieving data from DataFrame

Panda data storing format is similar to a dictionary, not a list of dictionary
```
a = covid_df['date']        # a series of data is stored in a
```
Each column is represented using a data structure called `Series`
```
type(covid_df['date'])                          # pandas.core.series.Series
covid_df['new_cases'][246]                      # Retrieving specific element
covid_df.at[246, 'new_cases']                   # Retrieving specific element by at method
covid_df.date                                   # Pandas also allows accessing columns as properties of the dataframe using the `.` notation instead of `[]`
covid_df[['date', 'new_cases']]                 # Retrieving a list of columns within the indexing notation []
cases_df = covid_df[['date', 'new_cases']]      # cases_df and covid_df both point to the same data in the computer's memory. Changing one will change the other.
covid_df_copy = covid_df.copy()                 # covid_df_copy is completely separate from covid_df
covid_df.loc[243]                               # To access a specific row of data
covid_df.loc[108:113]
type(covid_df.loc[243])                         # pandas.core.series.Series
covid_df.head(5)                                # To view the first few rows of data
covid_df.tail(4)                                # To view the last few rows of data
b = covid_df.at[0, 'new_tests']                 # nan is stored
type(covid_df.at[0, 'new_tests'])               # numpy.float64
covid_df.new_tests.first_valid_index()          # To find the first index that doesn't contain a NaN value using first_valid_index method.
covid_df.sample(10)                             # To retrieve a random sample of rows from the data frame.
total_cases = covid_df.new_cases.sum()          # To find the total value
```

> Querying and sorting rows 

```
high_new_cases = covid_df.new_cases > 1000          # high_new_cases is a series containing True and False boolean values
covid_df[covid_df.new_cases > 1000]                 # Querying a subset of rows satisfying the chosen criteria using boolean expressions
df['pos_rate'] = df.new_cases/df.new_tests          # Adding new columns by combining data from existing columns
covid_df.drop('positive_rate')                      # Removing one or more columns from the data frame
covid_df.drop(columns=['positive_rate'], inplace=True)
sort_values                                         # Sorting the rows of a data frame using column values
covid_df.sort_values('new_cases').head(10)
covid_df.sort_values('new_deaths', ascending=False).head(10)
covid_df.at[172, 'new_cases'] = ...                 # Replacing a value within the data frame
```

> Changing display option

```
from IPython.display import display
with pd.option_context('display.max_rows', 100):
    display(covid_df[covid_df.new_cases > 1000])
```

> Working with dates

```
covid_df['date'] = pd.to_datetime(covid_df.date)        # To convert it into a column of datetime datatype using the pd.to_datetime

# To extract different parts of the datatime datatype using the DatetimeIndex class
covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday
```

> Finding different statistics

```
covid_df.new_cases.mean()
covid_df[covid_df.weekday == 6].new_cases.mean()
```

> Grouping and Aggregation

We have to use the groupby function to create a group for each month, select the columns we wish to aggregate, and aggregate them using the sum (any statistics) method.
```
covid_month_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()
covid_month_mean_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].mean()
```

We can use the cumsum method to compute the cumulative sum of a column as a new series

```
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
covid_df['total_tests'] = covid_df.new_tests.cumsum() + initial_tests           # NaN values in the total_tests column remain unaffected.
```

> Merging data from multiple source

To merge two data frames, we need at least one common column.

```
# To add the columns from `locations_df` into `covid_df` using the `.merge` method.
merged_df = covid_df.merge(locations_df, on="location")
```