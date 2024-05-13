#  Polymorphism in Functions
# Problem:
# Write a function multiply that multiplies
# two numbers, but can also accept and multiply strings.


a = input("Enter the first number:")

b = input("Enter the second number:")

if not a or not b:
    print("Please enter both numbers")
    exit()


def multiply(a, b):
    return int(a) * int(b)


print(f"Multiplication of {a} and {b} is {multiply(a, b)}")
