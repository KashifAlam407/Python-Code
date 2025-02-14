# Sum of first n natural no.

num = int(input("Enter the number: "))
n = 0     # if we write 1 here then 1 is added to the result 
for i in range(0, num+1):  # if we do not write 1 here then programm also gives true result because here addition is performed
    n = n + i
print("The sum of first " + str(num) + " natural number is " + str(n))


