# to check which no. is greater

def maximum(num1, num2, num3):

## 1   
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3

## 2
    if(num1>num2) and (num1>num3):
        return num1
    elif(num2>num3) and (num2>num1):
        return num2
    else:
        return num3

m = maximum(1530, 550, 2200)
print("The maximum number is " + str(m))