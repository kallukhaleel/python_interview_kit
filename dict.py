#Sample Output: {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}



dict = {}
for i in range(ord('a'),ord('z')):
    dict [chr(i)] = i
print(dict)



#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples



Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
list2 = list1[::-1]
print("Expected Result:", list2)
