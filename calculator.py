"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

print("Welcome to the calculator! Please enter an operand followed by the numbers -this is a prefix calculator!")
while True:

    calculator_input = (input("> "))
    equation_list = calculator_input.split(' ')
    if equation_list[0] == 'q':
        break
    if len(equation_list)<2:
            print("input numbers are not enough")
    if len(equation_list)>1:
        equation_list[1] = int(equation_list[1]) 
    if len(equation_list)>2:
        equation_list[2] = int(equation_list[2]) 
    
    num1 = equation_list[1]
    num2 = equation_list[2]

    if equation_list[0] == '+':
        print(add(equation_list[1], equation_list[2]))
    elif equation_list[0] == '-':
        print(subtract(equation_list[1], equation_list[2]))
    elif equation_list[0] == '*':
        print(multiply(equation_list[1], equation_list[2]))
    elif equation_list[0] == '/':
        print(divide(equation_list[1], equation_list[2]))
    elif equation_list[0] == 'square':
        print(square(equation_list[1]))
    elif equation_list[0] == 'cube':
        print(cube(equation_list[1]))
    elif equation_list[0] == 'pow':
        print(power(num1, num2))
    elif equation_list[0] == 'mod':
        print(mod(num1, num2))
    
    




# Replace this with your code
