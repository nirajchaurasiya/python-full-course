#  Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong".
# Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
password = input("Enter your password to check:\n")

if password == "":
    print("Please enter a password to search")
    exit()

password_length = len(password)

if password_length < 6:
    strength = "Weak"

elif password_length <= 10:
    strength = "Medium"

else:
    strength = "Strong"

print("Password strength is", strength)
