# factorial method
# n! = 1 * 2 * 3 * ......* n
# 5! = 1 * 2 * 3 * 4 * 5 

num = int(input("Enter the number: "))
factorial = 1  # dont enter 0 becacuse the result is multiplied from 0 and becomes 0 as result
for i in range(1, num+1):
    factorial = factorial * i
print("The factorial of " + str(num) + " is " + str(factorial))
# print(f"The factorial of {num} is {factorial}")  # here you can also write 5th line with this method but my laptop is not responding me