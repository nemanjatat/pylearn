# logical operators = evaluate multiple conditions (or, and, not)
#                     or  = at least one condition must be true
#                     and = both conditions must be true
#                     not = inverts the condition (not false, not true)

items = ["pencil", "book", "ruler"]

add_item = input("Add a new item: ")

if add_item not in items:
    items.append(add_item)
    for item in items:
        print(item)
else:
    print("That item already exists in the list!")