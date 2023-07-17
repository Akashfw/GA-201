def is_palindrome(number):

    number_str= str(number)
    rever_str= number_str[::-1]
    if number_str== rever_str:
        return True
    else:
        return False



number = int(input("Enter a number : "))
if(is_palindrome(number)):
    print(f"{number} is a Palindrome")
else:
    print(f"{number} is not a Palindrome")
