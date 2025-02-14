# # ###
# # def even(n):
# #     return n%2==0
# my_list = [4,5,3,6,2,9,7,2]

# b = list(filter(lambda x : (x % 2 == 0), my_list))
# # b = list(filter(even, my_list))
# # b = set(filter(even, my_list))   ## you can change the class
# # # a = lambda b:b*b
# print(b)



## 
# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221]
j = [3,4,35,563,623,23,90,7]

# use anonymous function to filter
# result = list(filter(lambda x: (x % 13 == 0), my_list))
result = list(map(lambda x: (x * 2), j))    ## here map is used to change all the value of the list
# result = list(map(my_list*3), j)

# display the result
# print("Numbers divisible by 13 are",result)
print(result)
