import random
sides_of_die = int(input("How many sided dice do you want to roll? "))
dice = random.randint(1, sides_of_die)
print(dice)
keep_on_rolling = True
while keep_on_rolling:
    userDecision = input("Do you want to roll the dice again? ")
    if userDecision == "Yes":
        dice = random.randint(1, sides_of_die)
        print(dice)
    elif userDecision == "No":
        keep_on_rolling = False
print("Dice Program Terminated.")