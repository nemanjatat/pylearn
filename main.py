# conditional expression = a one-line shortcut for the if-else statement (ternary operator)
#                          print or assign one of two values based on condition
#                          x if condition else y

positive_or_negative_num = 6
even_or_odd_num = 2
a = 10
b = 13
age = 20
temperature = 30
user_role = "admin"

pos_neg_result = ("POSITIVE" if positive_or_negative_num >= 0 else "NEGATIVE")
print(pos_neg_result)
even_or_odd_result = ("EVEN" if even_or_odd_num % 2 == 0 else "ODD")
print(even_or_odd_result)
max_num = (f"{a} is greater than {b}" if a > b else f"{b} is greater than {a}")
print(max_num)
min_num = (f"{a} is lower than {b}" if a < b else f"{b} is lower than {a}")
print(min_num)
age_check = ("ADULT" if age >= 18 else "CHILD")
print(age_check)
temp_status = ("HOT" if temperature > 20 else "COLD")
print(temp_status)
access_level = ("FULL ACCESS" if user_role == "admin" else "LIMITED ACCESS")
print(access_level)