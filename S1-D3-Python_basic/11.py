n = 5

for i in range(1, n + 1):
    numbers = [str(num) for num in range(1, i + 1)]
    pattern = ", ".join(numbers)
    print(pattern)
