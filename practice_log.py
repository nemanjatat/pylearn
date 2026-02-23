items = []

while True:
    print("What would you like to do?")
    user_input = input("1. show list of items\n2. add an item\n3. quit\nChoose: ")

    if user_input == "1":
        if not items:
            print("The list is currently empty")
        else:
            print("Here is a list of your items:\n")
            for item in items:
                print(item)
    elif user_input == "2":
        new_item = input("What are you adding?: ")
        items.append(new_item)
    elif user_input == "3":
        break
    else:
        print("Invalid command")

print("Program exited")