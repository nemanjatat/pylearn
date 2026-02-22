# logical operators = evaluate multiple conditions (or, and, not)
#                     or  = at least one condition must be true
#                     and = both conditions must be true
#                     not = inverts the condition (not false, not true)

age = int(input("How old are you: "))
has_membership = input("Do you have a membership (Y/N): ")

if age >= 18 and has_membership == "Y":
    print("You are 18 or older and have a membership!")
else:
    print("You are either below 18 y/o or don't have a membership")