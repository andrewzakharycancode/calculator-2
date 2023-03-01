"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
userInput = ['']
while userInput[0] != 'q':
    userInput = input('> ').split(' ')
    print(userInput)