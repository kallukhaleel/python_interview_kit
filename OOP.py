'''OOP Assignment
Challenge 1: Square Numbers and Return Their Sum
🔴 In this challenge, you need to implement a method that squares passing variables and returns their sum.

Problem statement: Implement a class Point that has three properties and a method. All these attributes (properties and methods) should be public. This problem can be broken down into two tasks:

Task 1: 👉 Implement a constructor to initialize the values of three properties: x, y, and z.

Task 2: 👉 Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum.

Sample properties 1, 3, 5

Sample method output 35

image1

Coding exercise Create a class Point with three properties: x, y, and z.

class Point:

    def __init__(self):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        pass


'''


class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sqSum(self):
        sum = self.x **2 + self.y ** 2 + self.z ** 2
        return sum
val = Point(1,3,5)
val.sqSum()

'''

Output: 35

'''




'''
Task 2

👉 Methods

• add() is a method that returns the sum of num1 and num2.
• subtract() is a method that returns the subtraction of num1 from num2.
• multiply() is a method that returns the product of num1 and num2.
• divide() is a method that returns the division of num2 by num1.
Input - Pass numbers (integers or floats) in the initializer.

Output - addition, subtraction, division, and multiplication

Sample input

obj = Calculator(10, 94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()
Sample output

104
84
940
9.4
Coding exercise

class Calculator:

    def __init__(self):
        pass
    def add(self):
        pass
    def subtract(self):
        pass
    def multiply(self):
        pass
    def divide(self):
        pass


'''



class Calculator:
    def __init__(self,num1,num2):
        self.n1 = num1
        self.n2 = num2
        print( "Calculator Instance has been created")
        
    def add(self):
        sum = self.n1 + self.n2
        print(f'Sum of {self.n1} + {self.n2} = {sum}')
    def substract(self):
        sum = self.n1 - self.n2
        print(f'Total of {self.n1} - {self.n2} = {sum}')
    
    def multiply(self):
        sum = self.n1 * self.n2
        print(f'Total of {self.n1} * {self.n2} = {sum}')
    def divide(self):
        sum = self.n1 // self.n2
        print(f'Total of {self.n1} / {self.n2} = {sum}')
obj = Calculator(20,5)
obj.add()
obj.substract()
obj.multiply()
obj.divide()



'''


Output:

Calculator Instance has been created
Sum of 20 + 5 = 25
Total of 20 - 5 = 15
Total of 20 * 5 = 100
Total of 20 / 5 = 4


'''





''' 
Challenge 3: Implement the Complete Student Class
🔴In this challenge, you will implement a student class
Problem statement

Implement the complete Student class by completing the tasks below

Task

👉 Implement the following properties as private:

• name
• rollNumber
👉 Include the following methods to get and set the private properties above:

• getName()
• setName()
• getRollNumber()
• setRollNumber()
👉 Implement this class according to the rules of encapsulation.

Input - Checking all the properties and methods

Output - Expecting perfectly defined fields and getter/setters

Note: Do not use initializers to initialize the properties. Use the set methods to do so.

If the setter is not defined properly, the corresponding getter will also generate an error even if the getter is defined properly.

Coding exercise

class Student:

    def setName(self):
        pass
    def getName(self):
        pass
    def setRollNumber(self):
        pass
    def getRollNumber(self):
        pass
'''


class Student:
    def __init__(self,name = None,roll_no = None):
        self.__name = name
        self.__roll_no = roll_no
        
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setRollNumber(self,roll_no):
        self.__roll_no = roll_no
    def getRollNumber(self):
        return self.__roll_no
    
student = Student()
student.setName("Khaleel")
student.getName() # Khaleel
# khaleel.__name #Error
student.setRollNumber(21)
student.getRollNumber() #21




