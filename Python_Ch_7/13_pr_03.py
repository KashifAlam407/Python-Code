# Multiplication table

num = int(input("Enter the number: "))
i = 1
while i < 11:
    print(str(num) + " x "+str(i) + " = " + str(num*i))
    i = i+1