# Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or
# unripe based on its color.
# (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

color = input("Enter the fruit color:\n")

fruit = "Banana"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
