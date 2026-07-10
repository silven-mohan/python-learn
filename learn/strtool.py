# STRING TOOLKIT:

text= input("Enter any string: ")

print("     ==== STRING TOOLKIT ====")
print("1. Display string", "2. Length of the string", "3. Indexing", "4. Slicing", "5. Concatenation", "6. Repition", "7. Membership Operations", sep="\n")
choice = int(input("Choose one operation: "))

if choice == 1:
    print(f"The string is {text}")
elif choice == 2:
    print(f"The Length of the string {text} is: {len(text)}")
elif choice == 3:
    print("     == Indexing ==")
    print("1. Front", "2. Last", "3. Custom Index", sep="\n")
    choice1 = int(input("Choose any one of the option: "))

    if choice1 == 1:
        print(text[0])
    elif choice1 == 2:
        print(text[-1])
    elif choice1 == 3:
        index = int(input("Enter the index: "))

        if index >= len(text):
            print(f"Index: {index} is out of bounds")
            exit()
        
        print(text[index])
    else:
        print("Invalid option! Try again")
        exit()
elif choice == 4:
    print("     == Slicing == ")
    print("1. First n characters", "2. Last n characters", "3. Every second character", "4. Reverse", "5. Custom slice", sep="\n")
    choice1 = int(input("Choose one of the option: "))

    if choice1 == 1:
        n = int(input("Enter n: "))
        if n >= len(text):
            print("Out of bounds!!")
            exit()

        print(text[:n])
    elif choice1 == 2:
        n = int(input("Enter n: "))
        if n >= len(text):
            print("Out of bounds!!")
            exit()
        
        print(text[-n:])
    elif choice1 == 3:
        print(text[::2])
    elif choice1 == 4:
        print(text[::-1])
    elif choice1 == 5:
        start = int(input("Enter starting index: "))
        end = int(input("Enter ending index: "))
        step = int(input("Enter the stepping index: "))
        if step == 0:
            print("Step can't be zero")
            exit()

        print(text[start:end:step])
    else:
        print("Invalid option! Try again")
        exit()
elif choice == 5:
    text1 = input("Enter new string: ")

    print("Concatenated string: %s" % (text + text1))
elif choice == 6:
    n = int(input("Enter the no. of times for repition: "))
    if n <= 0:
        print("Repition can't be zero or less than zero.")
        exit()

    print(text * n)
elif choice == 7:
    print("     == Needle in haystack ==")
    print(f"Enter the needle the is to searched in the haystack {text}: ")
    needle = input()

    if needle in text:
        print("Needle is in the haystack")
    if needle not in text:
        print("Needle is not in the haystack")
else:
    print("Invalid option! Try again!!")
    exit()