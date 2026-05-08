# Factorial of a number:
# This program takes a number from the user and prints the factorial of that number.

# Taking the number from the user:
NUM = int(input("Enter any number: "))
fact = 1

# Calculating the factorial of NUM:
i = 2
while i <= NUM:
    fact *= i
    i += 1

# Printing the factorial of the given number:
print(f"The Factorial of {NUM} is: {fact}")