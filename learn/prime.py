# Prime Number Detector:
# This program takes any number from the user and checks whether the given number is prime or not.

# Taking the number from the user:
num = int(input("Enter any number: "))

# Checking for 1 or 0:
if num == 0 or num == 1:
    print("The number is neither prime nor composite.")
    exit()


i = 2
while i <= num/2:
    if num % i == 0:
        print(f"The number {num} is not a prime number.")
        exit()
    i += 1

print(f"The number {num} is a prime number.")