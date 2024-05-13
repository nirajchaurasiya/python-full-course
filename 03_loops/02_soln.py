# Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

num = int(input("Enter a number:"))
count = 0
for n in range(num):
    if n % 2 == 0:
        count += 1

print(count)
