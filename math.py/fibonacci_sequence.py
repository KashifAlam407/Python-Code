def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return (fibonacci(n-1)+fibonacci(n-2))
for i in range(1,11):
    print(fibonacci(i))

# fibonacci()

###
# num = int(input("Enter the number: "))
# n1, n2 = 0, 1
# sum = 0
# if num == 0:
#     print("Please enter number greater than 0")
# elif num == 1:
#     print(0)
# else:
#     for i in range(0, num):
#         print(n1,n2,sum)
#         n1 = n2
#         n2 = sum
#         sum = n1 + n2
        
        
###
# Python program to display the Fibonacci sequence

# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = 10

# check if the number of terms is valid
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
# for i in range(nterms):
#     print(recur_fibo(i))