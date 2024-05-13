#  Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100),
# B (80-89), C (70-79), D (60-69), F (below 60).

score = int(input("Enter your grade:\n"))

if score >= 101:
    print("Please verify your grade again")
    exit()

if score >= 90:
    print("You got an A grade")
elif score >= 80:
    print("You got a B grade")
elif score >= 70:
    print("You got a C grade")
elif score >= 60:
    print("You got a D grade")
else:
    print("You got an F grade")
