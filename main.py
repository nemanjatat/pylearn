# variable = a container for a value (string, integer, float, boolean)
#            a variable behaves as if it was the value it containts

# string
name = "nem"
item = "pen"
email = "nem@notrealemail.com"

print(f"Your name is: {name}")
print(f"You've picked up a new item!\nItem: {item}")
print(f"That guy's email is: {email}")

# integers
age = 29
stock = 5
num_of_people_at_event = 1549

print(f"Your age is: {age}")
print(f"Current stock: {stock}")
print(f"The number of people at the event is: {num_of_people_at_event}")

# floats
price = 10.99
gpa = 4.4
distance = 10.5

print(f"The price for that is {price}$")
print(f"Their gpa is: {gpa}")
print(f"That location is {distance}km away")

# booleans
is_student = False
for_sale = True
is_online = True

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT for sale")

if is_online:
    print("Friend is currently online")
else:
    print("Friend is currently offline")

# assignment

username = "@nem"
year = 2026
pi = 3.14
is_admin = True

print("=======================")
print("loading user info")
print("=======================")

print(f"Username: {username}")
print(f"Account created in year: {year}")
print(f"Pi value: {pi}")
print(f"User is admin: {is_admin}")