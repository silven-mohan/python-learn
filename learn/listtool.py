# LIST TOOLKIT:

LIST = list(map(int, input("Enter the all of the elements of the list separated by spaces: ").split()))

print("     ==== LIST TOOLKIT ====")
print("1. Display list", "2. Length of the list", "3. Indexing", "4. Slicing", "5. Append", "6. Insert", "7. Remove", "8. Pop", "9. Extend", "10. Sort", sep="\n")
print("11. Count of an element", "12. Index of an element", sep="\n")
choice = int(input("Choose one operation: "))

if choice == 1:
    print(f"The list is {LIST}")
elif choice == 2:
    print(f"The Length of the list {LIST} is: {len(LIST)}")
elif choice == 3:
    print("     == Indexing ==")
    print("1. Front", "2. Last", "3. Custom Index", sep="\n")
    choice1 = int(input("Choose any one of the option: "))

    if choice1 == 1:
        print(LIST[0])
    elif choice1 == 2:
        print(LIST[-1])
    elif choice1 == 3:
        index = int(input("Enter the index: "))

        if index >= len(LIST) or index < -len(LIST):
            print(f"Index: {index} is out of bounds")
            exit()
        
        print(LIST[index])
    else:
        print("Invalid option! Try again")
        exit()
elif choice == 4:
    print("     == Slicing == ")
    print("1. First n members", "2. Last n members", "3. Every second member", "4. Reverse", "5. Custom slice", sep="\n")
    choice1 = int(input("Choose one of the option: "))

    if choice1 == 1:
        n = int(input("Enter n: "))
        if n >= len(LIST) or n < -len(LIST):
            print("Out of bounds!!")
            exit()

        print(LIST[:n])
    elif choice1 == 2:
        n = int(input("Enter n: "))
        if n >= len(LIST) or n < -len(LIST):
            print("Out of bounds!!")
            exit()
        
        print(LIST[-n:])
    elif choice1 == 3:
        print(LIST[::2])
    elif choice1 == 4:
        print(LIST[::-1])
    elif choice1 == 5:
        start = int(input("Enter starting index: "))
        end = int(input("Enter ending index: "))
        step = int(input("Enter the stepping index: "))
        if step == 0:
            print("Step can't be zero")
            exit()

        print(LIST[start:end:step])
    else:
        print("Invalid option! Try again")
        exit()
elif choice == 5:
    num = int(input("Enter the element that is to be appended: "))
    LIST.append(num)

    print(f"The modified list is: {LIST}")
elif choice == 6:
    index = int(input("Enter the index of the element: "))
    if index >= len(LIST) or index < -len(LIST):
        print("Index is out of bounds!!")
        exit()
    
    num = int(input(f"Enter the element that is to be inserted at index: {index}"))

    LIST.insert(index, num)
    print(f"The modified list is: {LIST}")
elif choice == 7:
    num = int(input("Enter the value that should be removed from the list: "))
    if num in LIST:
        LIST.remove(num)
    else:
        print("Element is not in the list.")
        exit()
    
    print(f"The modified list is: {LIST}")
elif choice == 8:
    print("     == Pop == ")
    print("1. Pop by index", "2. Pop last element")
    choice1 = int(input("Choose one option: "))

    if choice1 == 1:
        index = int(input("Enter the index of the element: "))
        if index >= len(LIST) or index < -len(LIST):
            print("Index is out of bounds!!")
            exit()
            
        LIST.pop(index)
        print(f"The modified list is: {LIST}")
    elif choice1 == 2:
        LIST.pop()

        print(f"The modified list is: {LIST}")
    else:
        print("Invalid option! Try again")
        exit()
elif choice == 9:
    nLIST = list(map(int, input("Enter the all of the elements of the new list separated by spaces: ").split()))

    LIST.extend(nLIST)
    print(f"The modified list is: {LIST}")
elif choice == 10:
    print("     == Sort == ")
    print("1. Ascending", "2. Descending")
    choice1 = int(input("Choose one option: "))

    if choice1 == 1:
        LIST.sort()
        print(f"The sorted list is: {LIST}")
    elif choice1 == 2:
        LIST.sort(reverse = True)

        print(f"The sorted list is: {LIST}")
    else:
        print("Invalid option! Try again")
        exit()
elif choice == 11:
    num = int(input("Enter the value: "))
    print(f"The count of the element {num} in the list: {LIST} is: {LIST.count(num)}")
elif choice == 12:
    num = int(input("Enter the value: "))
    if num not in LIST:
        print("Element is not in the list.")
        exit()
    
    print(f"The index of the element {num} in the list: {LIST} is: {LIST.index(num)}")
else:
    print("Invalid option! Try again")
    exit()