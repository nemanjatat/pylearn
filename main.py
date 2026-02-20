# temperature conversion program

temperature = float(input("Enter temperature value: "))
unit = input("Is that in celsius or fahrenheit? (C or F): ")

if unit == "C":
    print(f"{temperature}{unit} is {temperature * (9/5) + 32}F")
elif unit == "F":
    print(f"{temperature}{unit} is {(temperature - 32) / (9/5)}C")
else:
    print(f"{unit} is not a valid unit!")