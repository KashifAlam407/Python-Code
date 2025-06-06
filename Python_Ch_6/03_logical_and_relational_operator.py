## 1. and operator

age = 45 
if(age>34 and age<56):  ## if both are true then executed 
    print("You can work with us")
else:
    print("You can not work with us")



## 2. or operator 

age = int(input("Enter your age: "))
if(age>34 or age<56):
    print("You can work with us")
else:
    print("YOu can not work with us")


## 3. not operator

age = int(input("Enter your age: "))
if(not(age>34)):  ## if age is not greater than 34 then executed it reverse the result as True of False
    print("You can work with us")
else:
    print("You can not work with us")