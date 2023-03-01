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
    print(f"user input tokenized: {userInput}")
    num1 = int(userInput[1])
    
    try:
        num2 = int(userInput[2])
    except:
        num2 = 0
    print(f"num2={num2}") 
    if userInput[0] == '+':
        result = add(num1, num2)
    elif userInput[0] == '-':
        result = subtract(num1, num2)
    elif userInput[0] == '*':   
        result = multiply(num1, num2)
    elif userInput[0] == '/':
        result = divide(num1, num2)
    elif userInput[0] == 'square':
        result = square(num1)
    elif userInput[0] == 'cube':
        result = cube(num1)
    elif userInput[0] == 'power':
        result = power(num1, num2)
    elif userInput[0] == 'mod':
        result = mod(num1, num2)
    print(result)