# Getting Started
"""
print("Hello World!")
print("Hi World!")
"""

# Variables
salary = 100000 # in RSD
bonus_rate = .10 # 10%
employee_name = "Dean"
company_name = "CompTech"

print(f"Employee Name: {employee_name}\nWorks For: {company_name}\nSalary: {salary}\n"
      f"Salary with bonus rate: {(salary * (1 + bonus_rate)):.0f}")

input()

job_id = 101
job_title = "Data Analyst"
job_salary = 125000
job_wfh = True # wfh = work from home

print("Job Description")
print("+++++++++++++++")
print("Job ID:        ", job_id)
print("Job Title:     ", job_title)
print("Job Salary:    ", job_salary)
print("Job WFH:       ", job_wfh)

# Python Terms

# Object: a data record with fields; an instance of a class
"""
salary = 100000
print(salary)
input()
print(type(salary))
input()
print(type("Data Analyst"))
input()
help(str)
"""
# Variables: The Reference to Objects
# Variables names themselves point to an object
# Variable: a defined name that references an object
"""
job_title = "Data Analyst"
job_location = "United States"
job_salary = 90000

print(id(job_title))
print(id(job_location))

# example of variables pointing (or identify) a specific object
job_1 = "Data Analyst"
job_2 = "Data Analyst"

print(id(job_1))
print(id(job_2))
input()

job_3 = job_1

print(id(job_1))
print(id(job_2))
"""
# you can assign anything to variables
my_print_func = print

my_print_func("Hi hello!")

# Function: A reusable piece of code that performs a special task.

# built-in function
print("Hi hello!")

# user defined function
def release_date():
      print("January 22nd")

release_date()

def movie_info(name, year, rating):
      print(f"Name:     {name}\nYear:     {year}\nRating:   {rating}")

movie_info("Seven Samurai", 1954, 8.6)

# Classes: The Template of Objects
# Class: A template for creating objects (records).

class JobPost:
      def __init__(self, title, location, salary):
            self.title = title
            self.location = location
            self.salary = salary

print(JobPost) # instance of a class

# Attributes: The Variables of an Object
# Attribute: A field in a record, defined by its class

class Animal:
      def __init__(self, species, diet, lifespan):
            self.species = species
            self.diet = diet
            self.lifespan = lifespan

animal_1 = Animal("Bald Eagle", "Carnivore", "20-30")
print(animal_1.species)

# The Functions of an Object
# Method: A function defined inside a class that operates on its objects.

class Device:
      def __init__(self, type, name, price):
            self.type = type
            self.name = name
            self.price = price
      def display_info(self): # method (function of a class)
            print(f"Type:      {self.type}\nName:      {self.name}\nPrice:     {self.price}")

laptop = Device("Laptop", "Asus TUF", 100000)
laptop.display_info()

print(help(int)) # we can see __add__ defined method in the int class

print(laptop.price.__add__(10000))