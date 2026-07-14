# Dictionary Toolkit

## Dictionary Creation:
stu = {
    "name" : "Silven",
    "age" : 18,
    "branch" : "CSE",
    "CGPA" : 9.5
}

print("     ==== Dictionary Toolkit ==== ")
print("1. Display", "2. Add new Key-Value", "3. Update", "4. Delete", "5. Search for a key", "6. Display Keys", "7. Display Values", "8. Display Key-Value pairs", sep = "\n")
print("9. Get a key", "10. Pop a key", "11. Pop an item", "12. Length of a dict", sep = "\n")
choice = int(input("Choose one of the option: "))

## Display:
if choice == 1:
    print(stu)

## Adding Key-Value:
elif choice == 2:
    key, value = map(str, input("Enter key and value: ").split())
    stu[key] = value
    print(stu)

## Update:
elif choice == 3:
    key, value = map(str, input("Enter the key and new value: ").split())
    stu.update({key : value})   ### OR: stu[key] = value
    print(stu)

## Delete a key:
elif choice == 4:
    key = input("Enter the key that is to deleted: ")

    del stu[key]
    print(stu)

## Search for a key:
elif choice == 5:
    key = input("Enter the key that is to searched in the dictionary: ")

    if key in stu:
        print("Key was found in the dictionary.")
    else:
        print("Key was not found in the key.")

## Display keys:
elif choice == 6:
    print(stu.keys())

## Display values: 
elif choice == 7:
    print(stu.values())

## Display key-value pairs:
elif choice == 8:
    print(stu.items())

## Get a key safely:
elif choice == 9:
    key = input("Enter a key: ")

    print(stu.get(key, "Key was not found."))

## Pops a key safely:
elif choice == 10:
    key = input("Enter a key: ")

    stu.pop(key, "Key was not found.")
    print(stu)

## Pops last-inserted key-value pair:
elif choice == 11:
    stu.popitem()

    print(stu)

## Length of a dictionary:
elif choice == 12:
    print("Length of the dictionary: ", len(stu))

## Error Case:
else:
    print("Invalid Option!! Try again..")
    exit()