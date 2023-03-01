"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
userInput = ['']
while userInput[0] != 'q':
    userInput = input('> ').split(' ')
    # userInput is always going to be a list
    # the first member of userInput (which is userInput[0]) is always going to be the operator (+, -, *, /, mod, pow, square, cube)
    # next two members of userInput is going to be num1 and num2
    print(userInput)
    num1 = int(userInput[1])
    num2 = int(userInput[2])
    if userInput[0] == '+':
        result = add(num1, num2)
    elif userInput[0] == '-':
        result = subtract(num1, num2)
    #elif userInput[0] == '*':   
        ## call multiply
    #elif userInput[0] == '/':
        ## call divide
    #elif userInput[0] == 'square':
        ## call square
    #elif userInput[0] == 'cube':
        ## call cube
    #elif userInput[0] == 'power':
        ## call power
    #elif userInput[0] == 'mod':
        ## call mod
    print(result)