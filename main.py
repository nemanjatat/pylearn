# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

last_digits = credit_number[-4:]
print(last_digits)

# or
last_digits = credit_number[15:]
print(last_digits)

print("============")
print("============")
print("============")

print(f"XXXX-XXXX-XXXX-{last_digits}")
user_input = input("fill in the missing numbers without (-):\n")

digits_no_hyphen = credit_number[0:15].replace("-", "")

if user_input == digits_no_hyphen:
    print("Correct!")
else:
    while True:
        user_input = input("Try again: ")
        if user_input == digits_no_hyphen:
            print("Correct!")
            break