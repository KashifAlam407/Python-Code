### 
# square = []
# for i in range(1,101):
#     square.append(i**2)
# print(square)

###
# squares2 = [i**2 for i in range(1, 101)]
# print(squares2 

###
# p = int(input("Enter the number: "))
# squares2 = [i**2 % p for i in range(1, p)]  # here len of remainder = (p+1)/2
# print(squares2)


## List comprehension  ##1
# square = [s for s in range(1,11) if s == 7]
# print(square)

##2
square = [s**2 for s in range(1,11) if s%2==0]
print(square)

###
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if ((i+j+k)!=n):
                    list.append([i,j,k])
    print(list)