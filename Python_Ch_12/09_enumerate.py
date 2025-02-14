## 1
# list1 = [3, 53, 2, False, 6.2,"Harry"]
# index = 0
# for item in list1:
#     print(item, index)
#     index += 1

## 2
list1 = [3, 53, 2, False, 6.2,"Harry"]
for index, item in enumerate(list1):
    print(index, item)


### 3
# print(list(enumerate(list1)))