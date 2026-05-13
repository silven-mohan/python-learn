# Leap Year Identification:
# This program takes any year from the user and checks whether it is a leap year or not.

# Taking the input:
year = int(input("Enter the year: "))

if year % 400 == 0:
    print(f"{year} is a Leap Year.")
elif year % 100 == 0:
    print(f"{year} is not a Leap Year.")
elif year % 4 == 0:
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")