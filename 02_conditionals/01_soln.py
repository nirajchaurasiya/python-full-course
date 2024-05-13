# Age Group Categorization

age = int(input("Enter your age: \n"))

if age < 13:
    print(f"User with age {age} is a child")
elif age < 20:
    print(f"User with age {age} is a teenager")
elif age < 60:
    print(f"User with age {age} is an adult")
else:
    print(f"User with age {age} is a senior")
