#                                   MADE BY MD KASHIF ALAM

#                                   HEART pattern in python 

num = int(input("Eneter the number of rows: "))
n = num//2
for i in range(n):
    for j in range(4-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    if num%2==0:
        for j in range()