## collatzSequence
## Write a function named collatz() that has one parameter named number.
## If number is even, then collatz() should print number // 2 and return this value.
## If number is odd, then collatz() should print and return 3 * number + 1.

import sys

try:
    def collatz():
        global number
        if number == 1:
            print('1')
            sys.exit()
        elif number % 2 == 0:
            number = (number // 2)
            print(number)
        elif number % 2 == 1:
            number = (3 * number + 1)
            print(number)

    print("Type a number")
    number = int(input())
    collatz()

    while number != 1 or number != 1.0:
        collatz()

except ValueError:
    print("That is not a number.\n\n\n", end='')
    print("--------------------------")
    sys.exit()
