# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

"""
sample input: 10

sample output: 35
"""

list1 = list(map(int,input().split()))
ans = list(map(lambda x: x + 25,list1))
print(ans)


"""
Output:
12 23 32 10 20
[37, 48, 57, 35, 45]
"""

"""
Write a Python program to triple all numbers of a given list of integers. Use Python map.


Input:
sample list: [1, 2, 3, 4, 5, 6, 7]

Triple of list numbers:

[3, 6, 9, 12, 15, 18, 21]

"""

list2 = list(map(int,input().split()))

tripled = list(map(lambda x : x *3, list2))
print(tripled)


"""
Output:

1 2 3 4 5 6
[3, 6, 9, 12, 15, 18]

"""

"""

Write a Python program to square the elements of a list using map() function.
Sample List: [4, 5, 2, 9]

Square the elements of the list:

[16, 25, 4, 81]

"""


list3 = list(map(int,input().split()))
sqr = list(map(lambda n : n ** 2,list3))
print(sqr)

"""
Output:

4 5 2 9
[16, 25, 4, 81]

"""
"""
Write a Python program to print even numbers from the list

"""


list4 = list(map(int, input().split()))

is_even = list(filter(lambda x : x % 2 == 0,list4))
print(is_even)



"""

Output:

Enter the elements: 1 2 3 4 5 6 7
[2, 4, 6]

        Here is some basic understanding of the functions like map, filter, reduce, and lambda.

        1. filter Function:
        Use Case: Filtering Elements in an Iterable:
        The filter function is used to filter elements from an iterable (e.g., a list) based on a specified condition.

        ==> It takes a function and an iterable as arguments and returns a new iterable containing only the elements for which the function returns True.

Example:
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Result: [2, 4, 6, 8, 10]

"""


      2. map Function:
      Use Case: Applying a Function to Each Element in an Iterable:
      The map function applies a specified function to each element in an iterable and returns a new one with the results.

      ==> It takes a function and one or more iterables as arguments.

Example:
"""
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
# Result: [1, 4, 9, 16, 25]

"""
      3. reduce Function:
      Use Case: Aggregating Elements in an Iterable:
      The reduce function is used to successfully apply a specified function to the elements of an iterable to reduce it to a single accumulated result.

      ==> It requires the functools module in Python 3 and takes a function and an iterable as arguments.

Example:
"""
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
# Result: 120

"""
      4. Lambda Functions:
      Use Case: Anonymous Functions:
      Lambda functions are small, anonymous functions defined using the lambda keyword.

      ==>  They are often used for short, one-time operations, especially as arguments to higher-order functions like filter, map, and reduce.

Example:
"""
add = lambda x, y: x + y
result = add(3, 5)
# Result: 8
        






