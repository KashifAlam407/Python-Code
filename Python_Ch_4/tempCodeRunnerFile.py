
###############  Ques 2   #################
x = ('hello')
y = ('hello',)

print(type(x))  # Output: <class 'str'>
print(type(y))  # Output: <class 'tuple'>

z = list(y)  # Converting tuple to list
print(z)  # Output: ['hello']
z[0] = 'Hello'
print(z)

z = tuple(z)  # Converting list back to tuple
print(z)  # Output: ('Hello',)
print(type(z))  # Output: <class 'tuple'>
# Converting a tuple to a list and back to a tuple
# print(type(tuple(z)))