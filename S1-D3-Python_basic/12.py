numbers = [45, 56, 160, 220, 370, 480, 505, 590, 660, 720]

for num in numbers:
    if num > 500:
        break  # Stop the loop if the number is greater than 500

    if num > 150:
        continue  # Skip the number if it is greater than 150

    if num % 5 == 0:
        print(num)
