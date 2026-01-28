# Program to demonstrate basic loops in Python
# for loop and while loop examples

# -------- for loop example --------
print("For loop example:")
for i in range(1, 6):
    print(i)


# -------- while loop example --------
print("\nWhile loop example:")
count = 1
while count <= 5:
    print(count)
    count += 1


# -------- loop with condition --------
print("\nChecking even numbers using loop:")
for num in range(1, 11):
    if num % 2 == 0:
        print(num, "is even")
