# input() = a function that prompts the user to enter data
#           returns the entered data as a string

new_item = input("What new item are you adding to the collection?: ")
item_stock = int(input(f"How many {new_item}s are you adding to the collection?: "))

print(f"You already have an extra {new_item}, +1")
item_stock += 1

print("============\nITEM INFO\n============")
print(f"New item added: {new_item}\nCurrent stock: {item_stock}")