# Program to demonstrate while loop in Python
# A while loop runs as long as a condition is True

# -------- Example 1: Basic while loop --------
# Initialization
count = 1

# Condition
while count <= 5:
    # Loop body
    print("Count:", count)

    # Update
    count += 1


# -------- Example 2: While loop with user input --------
# This example checks whether a number is positive or negative

number = int(input("\nEnter a number: "))

# Initialization
i = 1

# Condition
while i <= 1:
    if number > 0:
        print("The number is positive")
    elif number < 0:
        print("The number is negative")
    else:
        print("The number is zero")

    # Update (loop runs only once)
    i = i + 1


# -------- Example 3: Printing even numbers using while loop --------
num = 2  # Initialization

while num <= 10:  # Condition
    print(num)
    num = num +2       # Update
