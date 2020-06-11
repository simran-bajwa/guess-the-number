# Write a programme where the computer randomly generates a number between 0 and 20.
# The user needs to guess what the number is.
# If the user guesses wrong, tell them their guess is either too high, or too low

import random
real = random.randint(0, 20)

print("Instruction....blah blah")

no_o_attempts = 5
prev_guesses = []

while no_o_attempts > 0:
    print("You have ", no_o_attempts, " left")
    guess = int(input("Please make a guess"))
    while guess in prev_guesses:
        print("YOU HAVE GUESSED THIS NUMBER BEFORE")
        guess = int(input("Please make a guess"))
    prev_guesses.append(guess)
    if guess == real:
        print("the number you guessed is right")
        break
    elif guess > real:
        print("the number you guessed is too high")
    else:
        print("the number you guessed is too low")
    no_o_attempts -= 1

if guess == real:
    print("YOU WON")
else:
    print("YOU ARE A LOSER ;) \n better luck next time \n The correct number was ", real)