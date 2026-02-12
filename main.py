# input() = a function that prompts the user to enter data
#           returns the entered data as a string
"""
new_item = input("What new item are you adding to the collection?: ")
item_stock = int(input(f"How many {new_item}s are you adding to the collection?: "))

print(f"You already have an extra {new_item}, +1")
item_stock += 1

print("============\nITEM INFO\n============")
print(f"New item added: {new_item}\nCurrent stock: {item_stock}")
"""

# exercises

# rectangle area calc
"""
l = float(input("Enter length: "))
w = float(input("Enter width: "))

A = w * l

print(f"The area is {A}cm²") # ² = superscript (alt + 0178)
"""

# shopping cart program
item = input("What are you buying?: ")
price = float(input(f"What's the price for 1 {item}?: "))
quantity = int(input(f"How many {item}s, priced at {price} would you like to buy?: "))

total_price = quantity * price

print(f"Total price: {total_price}")