def add_lists(list1, list2):
    new_list = []
    length = max(len(list1), len(list2))

    for i in range(length):
        if i < len(list1) and i < len(list2):
            new_list.append(list1[i] + list2[i])
        elif i < len(list1):
            new_list.append(list1[i])
        else:
            new_list.append(list2[i])

    return new_list

# Example usage
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = add_lists(list1, list2)
print(result)
