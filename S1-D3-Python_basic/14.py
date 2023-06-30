def arrange_lowercase_first(string):
    lowercase = []
    uppercase = []

    for char in string:
        if char.islower():
            lowercase.append(char)
        else:
            uppercase.append(char)

    arranged_string = ''.join(lowercase + uppercase)
    return arranged_string

# Example usage
input_string = "aBcDeFgHiJkLmNoPqRsTuVwXyZ"
result = arrange_lowercase_first(input_string)
print(result)
