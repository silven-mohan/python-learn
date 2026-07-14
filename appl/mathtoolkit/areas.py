# Math Toolkit:

print("     ==== Math Toolkit ====     ")
print("1. Area Calculator")
choice = int(input("Chose one of the option: "))


if choice == 1:
    ## Area Calculator:
    print("1. Rectangle", "2. Circle", "3. Square", "4. Triangle", sep="\n")
    choice1 = int(input("Choose one option: "))

    ### Rectangle:
    if choice1 == 1:
        length, breadth = map(int, input("Enter the length and breadth of the rectangle: ").split())

        print("The area of the reactangle is: ", (length * breadth))
    
    ### Circle:
    elif choice1 == 2:
        radius = int(input("Enter the radius of the circle: "))

        print("The area of the circle is: ", (radius ** 2))
    
    ### Square:
    elif choice1 == 3:
        side = int(input("Enter the length of the side: "))

        print("The area of the square is: ", (side ** 2))
    
    ### Triangle:
    elif choice1 == 4:
        base, height = map(int, input("Enter the base and height of the triangle: ").split())

        print("The area of the triangle is: ", (0.5 * base * height))

    ### Error case:
    else:
        print("Invalid option!! Try again")
        exit()