"""
Write a Python function to sum all the numbers in a list.

Sample List : (8, 2, 3, 0, 7)

Expected Output : 20

Explanation:

Summation should like 8+2+3+0+7 = 20
"""

def sums(*list1):
    tot = 0
    for i in list1:
        tot +=i
    return tot
print(sums(2,3,5,5))

"""
Write a Python program to reverse a string.

﻿Sample String : "1234abcd"

Expected Output : "dcba4321"
"""


def sums(*list1):
    tot = 0
    for i in list1:
        tot +=i
    return tot
print(sums(2,3,5,5))

#Output
#Enter the string68tgylo,
#Here is the reverse of the given string:	 ,olygt86

"""
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.



﻿Sample String : 'The quick Brow Fox'

Expected Output :

No. of Upper case characters : 3

No. of Lower case Characters : 12
"""

def uplo(string):
    LowCase = 0
    UpCase = 0
    other = 0
    for x in string:
        if x.isupper():
            UpCase += 1
        elif x.islower():
            LowCase += 1
        else:
            other += 1
    print("No.of Lowercase is ",LowCase)
    print("No.of UpperCase is", UpCase)
    print("No.of Otherkeys is", other)
    return ""


Str = input("Let's check how many Lowercase and Uppercase in this string")
print(uplo(Str))

#Output
"""

Let's check how many Lowercase and Uppercase in this stringdfhu78erwhfqwehiofDFS
No.of Lowercase is  16
No.of UpperCase is 3
No.of Otherkeys is 2
"""




