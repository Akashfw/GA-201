
def factorial(n):
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

# Example usage
num = 5
factorial_result = factorial(num)
print("Factorial of", num, "is", factorial_result)




