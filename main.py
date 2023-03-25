import random
Rnumber = (random.randint(0,100))
print("... Generating Random Number ...")
tries = 0
print("A random number between 1 - 100 has been generated! Guess below:")
while tries < 1000:
    guess = input()
    guess = int(guess)

    tries = tries + 1
    if guess < Rnumber:
        print("Your number is too low! Try again!:")

    if guess > Rnumber:
        print("You guess is too high! Try again!")

    if guess == Rnumber:
        break

print("Congrats! You guessed the correct number of" , Rnumber, "in" , tries, "tries")