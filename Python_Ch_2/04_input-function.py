# a = input("Enter your name: ")
# a = int(a)  ## convert a to an integer (if possible)
# print(a)
# print(type(a))

# ## Taking multiple function in one line by using split() method:
# x, y = input("Enter two values: ").split()
# print(x)
# print(y)

## taking multiple inputs as a list
# x = list(map(int,input("Enter multiple values: ").split()))
# print(x)


# a, b = input("Enter two values: ").split()
# print("First number is {} and second number is {}".format(a, b))


## Taking multiple input at a time using list comprehension method
x,y = [int(x) for x in input("Enter multiple values: ").split()]
print(x)
print(y)


## Taking multiple input at a time using list comprehension method as a list
x = [int(x) for x in input("Enter multiple values: ").split()]
print(x)

## It can take both string and numbers also since input() by default take value as a string(integer given through input has string type)
x = [x for x in (input("Enter multiple values: ")).split()]
print(x)


# # taking multiple inputs at a time separated by comma
x = [int(x) for x in input("Enter multiple value: ").split(",")]
print("List is: ", x)


### In Python, when you use the print() function with multiple arguments separated by commas, Python automatically inserts a space between the arguments in the output
b = "for"
print("Geeks",b,"Geeks")  ## How space is printed b/w Geeks for Geeks


### using separator
### code for disabling the softspace feature
print('G','F','G', sep=' ')
 

#for formatting a date
# print('09','12','2016', sep='-')   ## it separates with whitespace
 
#another example
print('pratik','geeksforgeeks', sep='@')   ## it separates with @

# print(-7//3)
# print(9//3)
