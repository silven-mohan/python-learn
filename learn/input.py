# This shows all of the implementations of input() function.

name = input("Enter your name: ")
print("Hello,", name)

a = int(input("Now enter any number: "))
print("You've entered:", a)

a, b = map(int, input("Now enter any two numbers: ").split())
print("You've entered the numbers:", a, ",", b)