#1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. Finally print the list of the Employee objects.

import json
class Employee:
    
    def __init__(self, name, dob, height, city, state):
        self.name= name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state
​
    
with open('employee.json', 'r')as f:
    data = json.load(f)
    emp_list = []
    for emp_data in data['employees']:
        employee = Employee(emp_data['name'], emp_data['dob'], emp_data['height'], emp_data['city'], emp_data['state'])
        emp_list.append(employee)
for employee in emp_list:
    print('Name: ', employee.name)
    print('D.O.B: ', employee.dob)
    print('Hieght:', employee.height)
    print('City: ', employee.city)
    print('State: ', employee.state)
    print('\n')



"""
Name:  John
D.O.B:  1990-05-15
Hieght: 175
City:  New York
State:  New York


Name:  Alice
D.O.B:  1985-08-20
Hieght: 162
City:  Los Angeles
State:  California


Name:  Bob
D.O.B:  1987-12-10
Hieght: 180
City:  Chicago
State:  Illinois


Name:  Emily
D.O.B:  1992-03-25
Hieght: 168
City:  Houston
State:  Texas


Name:  Michael
D.O.B:  1983-09-05
Hieght: 185
City:  Miami
State:  Florida


Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
"""
indian_states = {
    "Uttar Pradesh": "Lucknow",
    "Maharashtra": "Mumbai",
    "Bihar": "Patna",
    "West Bengal": "Kolkata",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai",
    "Rajasthan": "Jaipur",
    "kerala": " Thiruvananthapuram"
}
​
import json
5
with open("states.json", "w+") as file:
    json.dump(indian_states, file, indent=5)
    print("file updated")

"""

file updated
Assignment 2 👉 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

🔴 a. It should have a function ‘description()’ which prints the name and age of the dog. 🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog. 🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own. 🔴 d. Create objects and implement the above functionalities.
"""
class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
        
    def description(self):
        print(f"\n Name of the dog: {self.name}\n Age: {self.age}")
        
    def get_info(self):
        print(f"\n Coat color: {self.coat_color}")
        
class JackRussel(Dog):
    def __init__(self, name, age, coat_color, height, weight):
        
        super().__init__(name, age, coat_color)
        self.height = height
        self.weight = weight
    
    def details(self):
        super().description()
        print(f"\n Hieght : {self.height}\n wEIGHT: {self.weight}")
        
    def barks(self):
        print(f"{self.name} barks ")
        
        
class BullDog(Dog):
    def __init__(self, name, age, coat_color, height, weight, life_existance):
        
        super().__init__(name, age, coat_color)
        self.height = height
        self.weight = weight
        self.life_existance = life_existance
    
    def details(self):
        super().description()
        print(f"\n Hieght : {self.height}\n wEIGHT: {self.weight}\n Life existance: {self.life_existance}")
        
    def barks(self):
        print(f"{self.name} barks ")
            
dog = JackRussel("Bob", 5, "black", '112cm', '22kg' )
dog.details()
"""
 Name of the dog: Bob
 Age: 5

 Hieght : 112cm
 wEIGHT: 22kg
​"""
dog.barks()
Bob barks 
bulldog = BullDog("Killer", 3, "white", '109cm', '12kg', 3)
bulldog.details()
"""
 Name of the dog: Killer
 Age: 3

 Hieght : 109cm
 wEIGHT: 12kg
 Life existance: 3
"""
