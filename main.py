#Python Variable
# a = 10
# b = 20
# c = a + b
# print(c)

#Python Data Types
# a = 10  integer
# b = 3.14  float
# c = "Hello, World!" string
# d = True boolean

#Python Data Structures
# List
# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# Tuple
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)
# Set   l
# my_set = {1, 2, 3, 4, 5}
# print(my_set)
# Dictionary
# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# print(my_dict)

#Python Operators
# Arithmetic Operators (+, -, *, /, %, **, //)
# a = 10
# b = 5
# print(a + b)  # Addition

#Comparison Operators (==, !=, >, <, >=, <=)
# a = 10
# b = 5
# print(a == b)  # Equal to
# print(a != b)  # Not equal to
# print(a > b)   # Greater than
# print(a < b)   # Less than
# print(a >= b)  # Greater than or equal to
# print(a <= b)  # Less than or equal to

#Logical Operators (and, or, not)
# a = True
# b = False
# print(a and b)  # Logical AND
# print(a or b)   # Logical OR
# print(not a)    # Logical NOT

#Assignment Operators (=, +=, -=, *=, /=, %=, **=, //=)
# a = 10
# a += 5  # Equivalent to a = a + 5
# print(a)  # Output: 15

#Bitwise Operators (&, |, ^, ~, <<, >>)
# a = 5  # In binary: 0101
# b = 3  # In binary: 0011
# print(a & b)  # Bitwise AND: 0001 (1 in decimal)
# print(a | b)  # Bitwise OR: 0111 (7 in decimal
# print(a ^ b)  # Bitwise XOR: 0110 (6 in decimal)
# print(~a)     # Bitwise NOT: 1010 (-6 in decimal)

#Identity Operators (is, is not)
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
# print(a is b)  # True, because a and b refer to the same object
# print(a is c)  # False, because a and c refer to different objects
# print(a == c)  # True, because a and c have the same content

#Membership Operators (in, not in)
# my_list = [1, 2, 3, 4, 5]
# print(3 in my_list)  # True, because 3 is in the list
# print(6 in my_list)  # False, because 6 is not in the list
# print(6 not in my_list)  # True, because 6 is not in the list

#Python Control Flow
# if statement
# a = 10
# if a > 5:
#     print("a is greater than 5")

# if-else statement
# a = 10
# if a > 5:
#     print("a is greater than 5")
# else:
#     print("a is not greater than 5")

# if-elif-else statement
# a = 10
# if a > 15:
#     print("a is greater than 15")
# elif a > 5:   

#Python Loops
# for loop
# for i in range(5):
#     print(i)

# while loop
# i = 0
# while i < 5:
#     print(i)
#     i += 1

#Python File Handling
#Create file in specific location
# with open("/home/home/Desktop/Python/data.txt", "w") as file:
#     file.write("File created")

# #Code to read the file
# with open("/home/home/Desktop/Python/data.txt", "r") as file:
#     content = file.read()
#     print(content)

#Code to append to the file
# with open("/home/home/Desktop/Python/data.txt", "a") as file:    file.write("\nThis is second line in file handling")

#Python Functions
# def greet(name):
    # return f"Hello, {name}!"
# print(greet("Jaffar")) 
    
def greet(name):
    print(f"Hello, {name}!")


user_name = input("Enter your name: ")
greet(user_name)
