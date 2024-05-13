# Pet Food Recommendation
# Problem: Recommend a type of pet food based on
# the pet's species and age.
# (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = input("Enter your pet species:'\n")

pet_age = input("Now, enter your pet age:'\n")

if pet == "Dog":
    if pet_age < 2:
        print("Puppy food")
    else:
        print("Adult food")

elif pet == "Cat":
    if pet_age > 5:
        print("Senior cat food")
    else:
        print("Baby cat food")
