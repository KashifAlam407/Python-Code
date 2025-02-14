# n! = (n-1)! * n
# sum(n) = sum(n-1) + n

# to add first n natural no.

# 1
# def add(n):
#     sum = 0
#     for i in range(n+1):
#         sum = sum + (i)
#     return sum

# s = add(9)
# print(s)

# 2
def add(n):
    sum = 0
    for i in range(n):
        sum = sum + (i+1)
    return sum

s = add(int(input("Enter the number: ")))
print(s)