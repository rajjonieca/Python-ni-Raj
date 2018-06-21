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
"""
class Employee(object):
    def __init__(self,emp):
        self.emp = emp
    def print_greetings(self):
        print("Hello ",self.emp)
    def calculate_wage(self,wage):
        total = wage * 12.0
        print("The salary of %s is %.2f " % (self.emp, total))
        print("-----------------------------------------------")

class PartTime(Employee):
    def print_greetings(self):
        print("Get to work ",self.emp,"! ")
    def calculate_wage(self,wage):
        total = wage * 20.0
        print("The wage of %s is %.2f " % (self.emp, total))
        print("-----------------------------------------------")

my_emp = Employee("Joyce")
my_emp.print_greetings()
my_emp.calculate_wage(90.0)

my_emp2 = PartTime("Samantha")
my_emp2.print_greetings()
my_emp2.calculate_wage(128.0)

my_emp3 = Employee("Kate")
my_emp3.print_greetings()
my_emp3.calculate_wage(75.0)
"""
"""
class MyCompany(object):
    def __init__(self,comp_name):
        self.comp_name = comp_name
        self.emp_list = {}
    def add_employee(self, name, wage):
        if not name in self.emp_list:
            self.emp_list[name] = wage
            print(name + " added!")
        else:
            print(name+ " existed")

    def print_employees(self):
        print("Welcome to ", self.comp_name)
        for empz in self.emp_list:
            print(empz +"\t" , self.emp_list[empz])
    def compute_salaries(self):
        total = 0
        for salaries in self.emp_list:
            total += self.emp_list[salaries]
        print("Main Total Expenses: %.2f " % (total))
        print("-------------------------------------------")

class BranchCompany(MyCompany):
    def add_employee(self, name, wage):
        if not name in self.emp_list:
            self.emp_list[name] = wage * 0.12
            print(name + " added!")
        else:
            print(name+ " existed")
    def print_employees(self):
        print("Welcome to ",self.comp_name)
        for empz in self.emp_list:
            print("%s \t %.2f" % (empz, self.emp_list[empz]))
    def compute_salaries(self):
        total = 0
        for salaries in self.emp_list:
            total += self.emp_list[salaries] * 0.10
        print("Total Expenses: %.2f " % (total))
        print("-------------------------------------------")
    def full_time_computation(self):
        return super(BranchCompany, self).compute_salaries()


comp1 = MyCompany("JCorp")
comp1.add_employee("Joyce",90.0)
comp1.add_employee("Kate",70.0)
comp1.add_employee("Angel",80.0)
comp1.add_employee("Joyce",90.0)
comp1.add_employee("Gena",80.0)
comp1.add_employee("Samantha",170.0)
comp1.print_employees()
comp1.compute_salaries()

brcomp = BranchCompany("JCorp Cabanatuan")
brcomp.add_employee("Mikhayla", 78.0)
brcomp.add_employee("Clarisse", 90.0)
brcomp.print_employees()
brcomp.compute_salaries()
print (brcomp.full_time_computation())
"""

"""
#Triangles
class Triangle(object):
  number_of_sides = 3
  def __init__(self,angle1,angle2,angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
  def check_angles(self):
    sum = self.angle1 + self.angle2 + self.angle3
    if sum == 180:
      return print(True)
    else:
      return print(False)

class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle
  def is_triangle(self):
    return super(Equilateral, self).check_angles()


tatsulok = Triangle(90.0, 45.0, 45.0)
tatsulok.check_angles()

my_triangle = Equilateral()
my_triangle.is_triangle()
"""






