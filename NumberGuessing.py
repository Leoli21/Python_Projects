import random
lower = ""
upper = ""
guess = 0
while not(lower.isnumeric()):
    lower = input("Lower Bound (Number): ")
while not(upper.isnumeric()):
    upper = input("Upper Bound (Number): ")
randnum = random.randint(int(lower),int(upper))
attempts = int(input("How many attempts to guess the number: "))
while int(guess) != randnum and attempts > 0:
    guess = input("Enter a guess: ")
    if int(guess) < int(randnum):
        print("Too low. Try again.")
        attempts = attempts - 1
    elif int(guess) > int(randnum):
        print("Too high. Try again.")
        attempts = attempts - 1
if attempts > 0 and (int(guess) == randnum):
    print("You correctly guessed the number " + str(guess) + " with " + str(attempts) + " attempts remaining.")
else:
    print("You failed to correctly guess the number.")


