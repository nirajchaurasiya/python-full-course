#  Movie Ticket Pricing

age = int(input("Enter your age:\n"))

day = "Wednesday"

price = 12 if age >= 18 else 8

# if age >= 18:
#     if day == "Wednesday":
#         print("Ticket price is $10 for adult")
#     else:
#         print("Ticket price is $12 for adult")

# else:
#     if day == "Wednesday":
#         print("The ticket price for a child is $6")
#     else:
#         print("The ticket price for a child is $8")

if day == "Wednesday":
    price -= 2
    if age >= 18:
        print(f"Ticket price for an adult is ${price}")
    else:
        print(f"Ticket price for a child is ${price}")
