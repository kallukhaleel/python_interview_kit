'''OOP Assignment
Challenge 1: Square Numbers and Return Their Sum
--------------------------------------------------------------------------------------------------------------------------------------------------------------

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

------------------------------------------------------------------------------------------------------------------------------------
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


'''
Challenge 4: Implement a Banking Account
----------------------------------------------------------------------------------------------------------------------------------------
🔴 In this challenge, you will implement a banking account using the concepts of inheritance.
Problem statement

Implement the basic structure of a parent class, Account, and a child class, SavingsAccount.

Task 1

👉 Implement properties as instance variables, and set them to None or 0.

Account has the following properties:

    • title
    • Balance
SavingsAccount has the following properties:

    • interestRate
Task 2

Create an initializer for Account class. The order of parameters should be the following, where Ashish is the title, and 5000 is the account balance:

Account("Ashish", 5000)

Task 3

Implement properties as instance variables, and set them to None or 0.

Create an initializer for the SavingsAccount class using the initializer of the Account class in the order below:

Account("Ashish", 5000, 5)

Here, Ashish is the title and 5000 is the balance and 5 is the interestRate.

image1

Coding exercise

class Account:

    def __init__(self):
        # write your code here
        pass

class SavingsAccount():

    def __init__(self):
        # write your code here
        Pass


'''

class Account:
    def __init__(self,title = None ,balance = 0,):
        self.title = title
        self.balance = balance
class SavingsAccounts(Account):
    def __init__(self, title, balance, rate = None):
        super().__init__(title, balance)
        self.rate = rate
    def InterestRate(self):
            print(f' Name : {self.title} \n Balance: {self.balance} \n Interesr Rate : {self.rate}')
            
            
acc1 = SavingsAccounts("Ashish",10000, 7)
acc1.InterestRate()



'''
Output:
 Name : Ashish 
 Balance: 10000 
 Interesr Rate : 7




Challenge 5: Handling a Bank Account
----------------------------------------------------------------------------------------------------------------------------------
🔴 In this challenge, you will define methods for handling a bank account using concepts of inheritance.

Problem statement

In this challenge, we will be extending the previous challenge and implementing methods in the parent class and its corresponding child class.

The initializers for both classes have been defined for you.

Task 1

In the Account class, implement the getBalance() method that returns balance.

Task 2

In the Account class, implement the deposit(amount) method that adds amount to the balance.

It does not return anything.

Sample input

balance = 2000
deposit(500)
getbalance()
Sample output

2500
Task 3

In the Account class, implement the withdrawal(amount) method that subtracts the amount from the balance.

It does not return anything.

Sample input

balance = 2000
withdrawal(500)
getbalance()
Sample output

1500
Task 4

In the SavingsAccount class, implement an interestAmount() method that returns the interest amount of the current balance.

Below is the formula for calculating the interest amount:

image1

Sample input

balance = 2000
interestRate = 5
interestAmount()
Sample output

100
The following figure shows what the result should logically look like:

image1

Coding exercise

Note: A new SavingsClass object is initialized at the end of the code and test results will be based on it.

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        # write code here
        pass

    def deposit(self, amount):
        # write code here
        pass
    def getBalance(self):
        # write code here
        pass

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        # write code here
        pass

#code to test - do not edit this

demo1 = SavingsAccount("Ashish", 2000, 5)   # initializing a SavingsAccount object


'''
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
        
        
    def withdrawal(self, amount):
        try:
            if (self.balance > 0 and self.balance > amount):
                
                self.balance -= amount
                print(f" Rs. {amount} has been withdrawn")
            else:
                print(f" Please maintain your balance: \n Your balance is {self.balance}")
        except Exception as e:
            print(f'Error{e}')

    def deposit(self, amount):
        self.balance += amount
        print(f" Rs. {amount} has been deposited")
    def getBalance(self):
        print(f' Total Amount of Mr. {self.title} is Rs. {self.balance}.00cr')
              
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        # interest amount = interest rate * balance // 100
        interestAmount = (self.interestRate * self.balance) / 100
        print(f' Interest amount of {self.title} is {interestAmount}')

#code to test - do not edit this

demo1 = SavingsAccount("Ashish", 2000, 5)   # initializing a SavingsAccount object
demo1.getBalance()
demo1.withdrawal(1000)

 # Total Amount of Mr. Ashish is Rs. 2000.00cr
 # Rs. 1000 has been withdrawn

demo1.getBalance()
demo1.interestAmount()
 # Total Amount of Mr. Ashish is Rs. 1000.00cr
 # Interest amount of Ashish is 50.0

demo1.deposit(100)
demo1.getBalance()
 # Rs. 100 has been deposited
 # Total Amount of Mr. Ashish is Rs. 1100.00cr

demo1.withdrawal(1200)
 # Please maintain your balance: 
 # Your balance is 1100

demo1.withdrawal(700)
​ # Rs. 700 has been withdrawn

demo1.interestAmount()
 # Interest amount of Ashish is 20.0
