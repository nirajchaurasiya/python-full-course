# Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

number = 5

mul = 1

# Method 1
# for n in range(number + 1):
#     if n == 0:
#         continue
#     else:
#         print(n)
#         mul *= n
# print(mul)

# Method 2
# for n in range(1, number + 1):

#     print(n)
#     mul *= n
# print(mul)

# Method 3
while number > 0:
    mul *= number
    number -= 1
print(mul)
