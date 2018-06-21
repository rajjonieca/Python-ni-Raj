import sys
import os

#This is lesson is all about classes
"""
class Girl(object):
    is_alive = True
    def __init__(self,name,age,school): #boots up the class
        self.name = name
        self.age = age
        self.school = school
    #Add method here
    def description(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("School: ", self.school)
        print("Is Alive: ", self.is_alive)


myGirl = Girl("Joyce",20,"AU")
print(myGirl.description)
"""
"""
class ShoppingCart(object):
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items_on_cart = {}

    def add_items(self,product,price):
        if not product in self.items_on_cart:
            self.items_on_cart[product] = price
            print(product + " added!")
        else:
            print(product + " already on the cart")

    def remove_item(self, product, price):
        if product in self.items_on_cart:
            del self.items_on_cart[product]
            print(product + " deleted!")
        else:
            print(product + "is not already in the cart")
    def print_items(self):
        print("Items on cart: ")
        for item in self.items_on_cart:
            print(item, "\t", self.items_on_cart[item])

custommer = ShoppingCart("Raj")
custommer.add_items("Condom",90)
custommer.add_items("Melon", 45)
custommer.add_items("Pistol", 7500)
custommer.remove_item("Condom",90)
custommer.print_items()
"""

"""
#Inheritance - one class takes the attributes of another class
class Vehicle(object):
    def __init__(self,number_of_wheels):
        self.number_of_wheels = number_of_wheels

class Lambo(Vehicle):
    def __init__(self, wheel1, wheel2, wheel3, wheel4):
        self.wheel1= wheel1
        self.wheel2 = wheel2
        self.wheel3 = wheel3
        self.wheel4 = wheel4
"""

#Override

class Employee(object):
    def __init__(self,emp):
        self.emp = emp
    def print_greetings(self):
        print("Hello ",self.emp)
    def calculate_wage(self,wage):
        total = wage * 12.0
        print("The salary of %s is %f " % (self.emp, total))

class PartTime(Employee):
    def print_greetings(self):
        print("Get to work ",self.emp,"! ")
    def calculate_wage(self,wage):
        total = wage * 20.0
        print("The wage of %s is %f " % (self.emp, total))

my_emp = Employee("Joyce")
my_emp.print_greetings()
my_emp.calculate_wage(90.0)

my_emp2 = PartTime("Samantha")
my_emp2.print_greetings()
my_emp2.calculate_wage(128.0)








