# value = 100

# # format the integer to binary
# binary_value = format(value, 'b')
# print(binary_value)



### Another code
def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)
