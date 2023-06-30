def append_in_middle(s1, s2):
    middle_index = len(s1) // 2
    s3 = s1[:middle_index] + s2 + s1[middle_index:]
    return s3

# Example usage
string1 = "Hello"
string2 = "World"
result = append_in_middle(string1, string2)
print(result)
