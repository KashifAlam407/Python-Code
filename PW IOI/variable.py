
#########################################################
### ================  PW IOI  ======================= ###
#########################################################

x = 10
print(x)

x = 20, 30, 40, 50, 60, 70, 80, 90, 100
print(x)

x, y, z = 10, 20, 30
print(x, y, z)

x = 5
y = 5
print(id(x), id(y))  # if the number is between -5 to 256, the id will be same


x = 2579
y = 2579
print(id(x), id(y))  # if the number is greater than 256, the id will be different


x = int(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
z = str(input("Enter the value of z: "))
print(x, y, z)
print(type(x), type(y), type(z))  # printing the type of variables


x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
print(x+y)  # addition
print(x-y)  # subtraction
print(x*y)  # multiplication
print(x/y)  # division (Gives the quotient with the decimal part)
print(x//y)  # floor division (Gives the quotient without the decimal part)
print(x%y)  # modulus
print(x**y)  # exponentiation


x = bool(input("Enter the value of x: "))
y = bool(input("Enter the value of y: ")) 
print(x and y)  # logical AND
print(x or y)  # logical OR 
print(not x)  # logical NOT
print(x is y)  # identity operator (checks if both are same)
print(x is not y)  # identity operator (checks if both are not same)
# print(x in y)  # membership operator (checks if x is in y)
# print(x not in y)  # membership operator (checks if x is not in y)
print(x > y)  # greater than
print(x < y)  # less than
print(x >= y)  # greater than or equal to
print(x <= y)  # less than or equal to
print(x == y)  # equal to
print(x != y)  # not equal to
 

x = 4
y = 6
print(x & y)  # bitwise AND
print(x | y)  # bitwise OR
print(x ^ y)  # bitwise XOR
print(x << y)  # left shift
print(x >> y)  # right shift
print(~x)  # bitwise NOT


## Swapping the values of x and y
x = 10
y = 20
print("Before swapping: x =", x, "y =", y)
x, y = y, x  # swapping the values of x and y
print("After swapping: x =", x, "y =", y)


x = (2, 3, 4, 5, 6, 7, 8, 9, 10)
y = 7
print(x)  # tuple
print(type(x))  # printing the type of variable
print(x[0])  # printing the first element of the tuple
print(x[1])  # printing the second element of the tuple
print(y in x)  # checking if y is in x
print(y not in x)  # checking if y is not in x
print(x.count(2))  # counting the number of times 2 is in x
print(x.index(2))  # printing the index of 2 in x
print(x.index(3, 0, 5))  # printing the index of 3 in x from index 0 to 5
print(x.index(3, 0, 4))  # printing the index of 3 in x from index 0 to 4
print(x.index(3, 0, 3))  # printing the index of 3 in x from index 0 to 3
print(x.index(3, 0, 2))  # printing the index of 3 in x from index 0 to 2
print(x.index(3, 0, 1))  # printing the index of 3 in x from index 0 to 1
print(x.index(3, 0, 0))  # printing the index of 3 in x from index 0 to 0
print(x.index(3, 0, -1))  # printing the index of 3 in x from index 0 to -1
print(x.index(3, 0, -2))  # printing the index of 3 in x from index 0 to -2
print(x.index(3, 0, -3))  # printing the index of 3 in x from index 0 to -3


#### Class Work ####
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
h = int(input("Enter the value of h: "))

Area = 1/2*(a+b)*h
print("Area of the triangle is: ", Area)

Area = 3**0.5*a**2/4
print("Area of the triangle is: ", Area)

exp = (a+b)**0.5*1/2*(a**2 + b**2)
print(exp)

s = (a+b+c)/2
print(s)

A = (s*(s-a)*(s-b)*(s-c))**0.5
print(A)

T = 2*22/7*(a/b)**0.5
print(T)


