# Create a dice-rolling game function. Your function should do the following; allow the player to enter a value r or q.
#  If they enter the letter r for roll the game loop will begin. Else, if they enter q they will quit the game and end the function.
#  When the user enters r, your function should randomly select a number between 1 and 7. If the player rolls a 7, they will win and they're score goes up by 10. 
# The game loop should ask them if they want to roll again or quit. If the player rolls anything other than 7 they will loss 5 points and be prompted to roll again or quit.
# To create this program you will need to use the randint() built in function. You can learn more about this using the w3schools article below

def dicegame():
    print("Just say now when you want me to role the number for you")
    
    import random

print(random.randint(3, 9))
