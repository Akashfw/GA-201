def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    if n <= 2:
        return fibonacci_sequence[:n]

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

# Example usage
num = 5
fibonacci_sequence = generate_fibonacci(num)
print(fibonacci_sequence)
