def factorial(i):
    if i == 0 or i == 1:
        return 1
    else:
        return i * factorial(i - 1)
    

dict1 = {i: factorial(i) for i in range(0, 11, 2)} 
print(dict1)


###----------------------------------
dict2 = {key: value**3 for key, value in range(1, 10) if (key % 3 == 0) elif (key % 4 == 0) value**2}

print(dict2)




###
# result = {}
# for num in range(1, 13):
#     if num % 3 == 0:
#         result[num] = num ** 3
#     elif num % 4 == 0:
#         result[num] = num ** 2

# print(result)