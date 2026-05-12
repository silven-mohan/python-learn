# Multiplication Tables Generator
# This program takes any number from the user and prints its multiplication upto 10 steps.

# Taking the number from the user:
num = int(input("Enter any number: "))

# Printing the multiplication table:
print(f"The Multiplication Table of {num} is: ")
print("==================")

i = 1
while i <= 10:
    print(f"{num} x {i} = {num*i}")
    i += 1

print("==================")