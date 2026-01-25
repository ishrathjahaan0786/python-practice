# Program to demonstrate nested if and if-elif-else statements in Python

# -------- Nested if example --------
number = int(input("Enter a number: "))

if number >= 0:
    if number == 0:
        print("The number is zero")
    else:
        print("The number is positive")
else:
    print("The number is negative")


# -------- if-elif-else example --------
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")
