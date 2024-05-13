#  Multiplication Table Printer
# Problem: Print the multiplication table for a given
# number up to 10, but skip the fifth iteration.

number = int(input("Enter a number:"))

for num in range(11):
    if num == 0 or num == 5:
        continue
    else:
        print(f"{number}*{num}=", number * num)
