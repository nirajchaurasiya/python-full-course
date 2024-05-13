# Validate Input
# Problem: Keep asking the user for input until they enter
#  a number between 1 and 10.

while True:
    input_num = int(input("Enter value between 1 and 10:"))

    if 1 <= input_num <= 10:
        break
    else:
        print(f"{input_num}! Invalid number. Try again")
print("Thanks for playing")
