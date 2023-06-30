

def add_person(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age

def delete_person(dictionary, name):
    if name in dictionary:
        del dictionary[name]

# Create an empty dictionary
people = {}

# Add "John": 25
add_person(people, "John", 25)
print(people)

# Update "John": 26
update_age(people, "John", 26)
print(people)

# Delete "John"
delete_person(people, "John")
print(people)
