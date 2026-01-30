# Program to demonstrate for loop in Python
# In a for loop, Python handles initialization, condition, and update automatically

# -------- Example 1: Basic for loop --------
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)


# -------- Example 2: For loop with condition --------
print("\nEven numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:
        print(num)


# -------- Example 3: For loop with user input --------
n = int(input("\nEnter a number: "))

print("Multiplication table of", n)
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
