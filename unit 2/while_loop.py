# Loop - a loop is a construct (special function) that repeats itself.
# in programming, a loop allows to repeat code instructions

# there are 2 types of loops: for loop and while loop

# while loop- a type of loop where so long as a condition is equal
# to true it will keep running"forever"

# the keyboard is while --> do while

#syntax
num = 4
while 2+2 == num: # condition --> operations - must be true
    print("the program is running...")


# while loops will ALWAYS run unless you change the condition!
# we can do this by writing instructions to manually change it.

def guessingGame():
    correctAnswer = 12
    attempts = 0

    print("GUESSING GAME HAS STARTED")
    userGuess = input("please guess a number between 1 and 50.")

    while userGuess != correctAnswer:
        print("incorrect, please try again...")
        attempts +=1
        userGuess = int(input("please guess a number between 1 and 50"))
    guessingGame()