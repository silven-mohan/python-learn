# String Palindrome Identifier
# This program verifies whether a given string is a palindrome or not.

# Taking input from the user.
text = input("Enter the string: ").replace(" ", "").lower()

# Validing if the input is string or not:
if not text.isalpha():
    print("Invlaid Input!!")
    exit()

# Checking if the string is a palindrome or not:
if text == text[::-1]:
    print(f"The given string {text} is a palindrome.")

else:
    print(f"The given string {text} is not a palindrome.")