# 2. Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
    # *Input*: 5, 0
    # *Output*: "Cannot divide by zero."

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Test the function
num1 = 5
num2 = 0
result = divide_numbers(num1, num2)
print(result)
