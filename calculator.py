"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

print("Welcome to the calculator! Please enter an operand followed by the numbers -this is a prefix calculator!")
while True:
    calculator_input = (input("> "))
    equation_list = calculator_input.split(' ')
    if equation_list[0] == 'q':
        break
    equation_list[1] = int(equation_list[1]) 
    equation_list[2] = int(equation_list[2]) 
    elif equation_list[0] == '+':
        print(add(equation_list[1], equation_list[2]))
    elif equation_list[0] == '-':
        print(subtract(equation_list[1], equation_list[2]))
    elif equation_list[0] == '*':
        print(multiply(equation_list[1], equation_list[2]))
    elif equation_list[0] == '/':
        print(divide(equation_list[1], equation_list[2]))




# Replace this with your code
