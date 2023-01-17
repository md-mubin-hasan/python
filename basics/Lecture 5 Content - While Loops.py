a = 10
while a > 0:
    print(a)
    a = a - 1
print('Finished')

import random
x = random.randint(1, 100)
y = random.randint(1, 100)

ans = x + y
print('What is ', x, '+ ', y, ' ?')
guess = int(input("? "))

while guess != ans:
    print('What is ', x, '+ ', y, ' ?')
    guess = int(input('? '))

print('You are right!')

"""
You can write a big comments inside thrice double brackets

infinite loop stop korte ctrl + C diye stop kora jabe
"""


