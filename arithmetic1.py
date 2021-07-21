def add(num_list):
    """Return the sum of the two inputs."""
    result = 0
    for num in num_list:
        result = result + num
    return result
# nums = [1, 3, 5, 6]
# print(add(nums))

def subtract(num_list):
    """Return the second number subtracted from the first."""
    result = num_list[0]
    for i in range(1, len(num_list)):
        result = result - num_list[i]
    return result
# nums = [10, 7, 3]
# print(subtract(nums))

def multiply(num_list):
    """Multiply the two inputs together."""
    result = 1
    for num in num_list:
        result = result * num
    return result
# nums = [2, 3, 3]
# print(multiply(nums))

def divide(num_list):
    """Divide the first input by the second and return the result."""
    result = num_list[0]
    for i in range(1, len(num_list)):
        result = result / num_list[i]
    return result
nums = [10, 2, 5]
print(divide(nums))

def square(num_list):
    square_list=[]
    for num in num_list:
        squares= num*num
        square_list.append(squares)
    return square_list
nums = [2, 4, 5]

print(square(nums))
        
  

def cube(num1):
    """Return the cube of the input."""
    return num1*num1*num1

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    return num1**num2

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    return num1%num2 