# guessTheNumber.py

#This is my iteration of the game with unlimited guesses. I did not look through the whole instruction of what he was looking for
#but rather saw what was generally looked for and tried to code it on my own
#the crux of this was me realizing that I needed to take the input() and convert it to an int
# the second half of this is the coe that is written in the book
# import random

# print('I am thinking of a number between 1 and 20.\n')
# print('Take a guess')
# guess = input()
# guess = int(guess)
# my_number = random.randint(1, 20)

# while guess != my_number:
#     if guess > 20:
#         print('Your guess is out of the range\nTake another guess')
#         guess = int(input())
#     elif guess <= 0:
#         print('Your guess is out of the range\nTake another guess')
#         guess = int(input())
#     elif guess < my_number:
#         print('Your guess is too low.\nTake another guess')
#         guess = int(input())
#     elif guess > my_number:
#         print('Your guess is too high.\nTake another guess')
#         guess = int(input())


# else:
#     print('You guessed the correct number!')



#here is the code from the book

#This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

#Ask the player to guess 6 times.
for guessesTaken in range (1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break  #This conidion is the correct guess

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


