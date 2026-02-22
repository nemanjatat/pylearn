name = input("Enter your full name: ")

print(len(name)) # is actually a function, not a method
print(name.find("a"))
print(name.rfind("a"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())

phone_number = input("Enter your phone number: ")

print(phone_number.count("-"))
print(phone_number.replace("-", ""))