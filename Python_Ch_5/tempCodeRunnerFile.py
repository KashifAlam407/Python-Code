result = {}
for num in range(1, 13):
    if num % 3 == 0:
        result[num] = num ** 3
    elif num % 4 == 0:
        result[num] = num ** 2

print(result)