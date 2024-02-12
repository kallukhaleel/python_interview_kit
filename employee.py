"""
Create an assignment for File handling of JSON files in Python
Assignment 1
👉 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class.
 Finally print the list of the Employee objects.
"""


import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

with open("data.json", 'r') as file:
    data = json.load(file)
    employee =[]
    for employees in data['employees']:
        emp_data = Employee(employees['name'], employees['dob'],  employees['height'], employees['city'], employees['state'])
        employee.append(emp_data)
for emp in employee:
    print(f"Name: {emp.name} 'DOB: ' {emp.dob} 'Height: '{emp.height} 'City'{emp.city} 'Sate'{emp.state}")
    print()

#output

"""
Name: John 'DOB: ' 1990-05-15 'Height: '175 'City'New York 'Sate'New York

Name: Alice 'DOB: ' 1985-08-20 'Height: '162 'City'Los Angeles 'Sate'California

Name: Bob 'DOB: ' 1987-12-10 'Height: '180 'City'Chicago 'Sate'Illinois

Name: Emily 'DOB: ' 1992-03-25 'Height: '168 'City'Houston 'Sate'Texas

Name: Michael 'DOB: ' 1983-09-05 'Height: '185 'City'Miami 'Sate'Florida
"""