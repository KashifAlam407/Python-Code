def factorial(i):
    if i == 0 or i == 1:
        return 1
    else:
        return i * factorial(i - 1)
    

dict1 = {i: factorial(i) for i in range(0, 11, 2)} 
print(dict1)


###----------------------------------
# This code snippet is an example of dictionary comprehension in Python.
# It creates a dictionary where the keys are numbers from 1 to 12, and the values are either the cube of the number if it is divisible by 3, or the square of the number if it is divisible by 4 but not by 3.
# It uses a conditional expression to determine the value for each key based on the specified conditions.
# The dictionary comprehension iterates over the range from 1 to 12, checking each number against the conditions and assigning the appropriate value.
# It uses a conditional expression to determine the value for each key based on the specified conditions.

dict2 = {key: key**3 if key%3==0 else key**2 for key in range(1, 13) if key%3==0 or (key%4==0 and key%3!=0)}
print(dict2)



dict2 = {
    x: x**3 if x % 3 == 0 else x**2  
    for x in range(1, 13)  
    if x % 3 == 0 or (x % 4 == 0 and x % 3 != 0)
}
print(dict2)
# This code snippet is an example of dictionary comprehension in Python.
# It creates a dictionary where the keys are numbers from 1 to 12.



###-----------------------------------# The following code snippet is an example of how to create a dictionary using a for loop and conditional statements.
# It creates a dictionary where the keys are numbers from 1 to 12, and the values are either the cube of the number if it is divisible by 3, or the square of the number if it is divisible by 4. 

# result = {}
# for num in range(1, 13):
#     if num % 3 == 0:
#         result[num] = num ** 3
#     elif num % 4 == 0:
#         result[num] = num ** 2

# print(result)