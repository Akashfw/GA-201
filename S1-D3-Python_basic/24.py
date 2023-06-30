# 1. Write a Python function that checks whether a given word or phrase is a palindrome.
    # *Input*: "madam"
    # *Output*: "The word madam is a palindrome."

def is_palindrome(word):
    word = word.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    reversed_word = word[::-1]  # Reverse the word
    if word == reversed_word:
        return f"The word {word} is a palindrome."
    else:
        return f"The word {word} is not a palindrome."

word = "madam"
result = is_palindrome(word)
print(result)
