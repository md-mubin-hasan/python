def plus():
    global a, b
    #global b
    return a+b

def square(number):
    return number * number

input_number = int(input("Please give me a number: "))
print("The square of the number is: ", end="")
print(square(input_number))
a = int(input("Please give me a number: "))
b = int(input("Please give me a number: "))
print(plus())

def donate(money):
    if money <= 0:
        # Stop the function when
        # the value is a silly one
        return

    # Print a message if the value is okay
    print("Thank you! You are so generous!")

donation = int(input("How much do you donate? "))
donate(donation)
