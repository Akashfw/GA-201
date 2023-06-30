def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Example usage
input_string = "Hello"
num_vowels = count_vowels(input_string)
print("Number of vowels:", num_vowels)
