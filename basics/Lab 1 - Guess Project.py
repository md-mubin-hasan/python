import random               # Import the 'random' library

target = random.randint(1,100)                  # We will store the number to be guessed here
finished = False            # This is true if the game has finished
guess_input_text = ""       # We will store text in here
guess_input = 0             # We will store a number in here

# Generate a new integer random number
print("I am thinking of a number. What number am I thinking of?")
count = 0
# Do the main game loop
while not finished:
    # Get the user's guess
    count = count + 1
    guess_input_text = input("Please enter a number between 1 and 100: ")
    guess_input = int(guess_input_text)
    # Check the user's guess
    if guess_input < 1 or guess_input > 100:
        print("Please enter an integer number between 1 and 100.")
    else:
        if guess_input == target:
            print("You got it! My number is " + str(target)+".")
            print("It took you " +str(count)+" guesses to get the number!")
            finished = True
        elif guess_input > target:
            print("Too high.")
        else:
            print("Too low.")

# At this point, the game is finished
