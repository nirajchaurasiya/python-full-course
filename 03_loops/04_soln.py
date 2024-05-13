#  Reverse a String
# Problem: Reverse a string using a loop

word = "Python"

reversed_str = ""

for char in word:
    reversed_str = char + reversed_str

print(reversed_str)
