"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
exitCond = 'a'
while exitCond != 'q':
    userInput = input('> ').split(' ')
    print(userInput)