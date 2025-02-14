## 1
# this will print the multiplication table of required number entered by user
num = int(input("Enter your number: "))
table = [num*i for i in range(1,11)]
print(table)

## 2
num = int(input("Enter your number: "))
for i in range(1,11):
    print(num*i)

## 3
num = int(input("Enter your number: "))
for i in range(1,11):
    print(f"{num} x {i} == {num*i}")
