# Guess the Number Game with Random Module and Loops:
# This program generates a random number and asks the user to guess it within a limited number of attempts.

import random
def guess():
    n = random.choice(range(1, 50)) #choosing number between 1 to 50
    a = 0 #no.of attempts
    ma = 5 #maximum no.of attempts
    print("The number is choosen. The Maximum number of attempts is",ma)

    while a < ma:
        guess = int(input("Enter the guess: "))
        a += 1

        if guess < n:
            print("Choose higher number")
        elif guess > n:
            print("Choose lower number")
        else:
            print("Right choice. The number has been guessed at ",a, "attempts")
            break
    else:
        print("Ran out of attempts.The number was", n)
guess()
