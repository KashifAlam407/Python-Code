x = int(input("Enter the number: "))
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
print(factorial(x))


# # num = 3
# num = int(input("Enter the number: "))
# print("The factorial of", num, "is", factorial(num))




####
# for x in range(2,20,2):

#     def factorial(x):
#         if x == 1:
#             return 1
#         else:
#             return (x + factorial(x-1))

# a = factorial(5)
# print(a)




####
# for x in range(2,20,2):

#     def factorial(x):
#         return (x + factorial(x+2))

#         # if x > 20:
#         #     print("villain died") 

# a = factorial()
# print(a)


# def fact():
#     fact()

# fact()

def is_leap(year):
    # leap = False
    
    # Write your logic here
    NotLeap = [1800, 1900, 2000, 2100, 2200, 2300, 2500]
    if (year % 4 == 0) and (year != year in NotLeap()):
        return True
    else:
        return False
    
    # return leap

year = int(input())
print(is_leap(year))




