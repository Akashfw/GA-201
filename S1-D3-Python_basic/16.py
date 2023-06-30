def concatenate_lists(list1, list2):
    new_list = []

    for item1 in list1:
        for item2 in list2:
            new_list.append(item1 + item2)

    return new_list

# Example usage
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = concatenate_lists(list1, list2)
print(result)
