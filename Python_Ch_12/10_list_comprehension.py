# ## 1
# a = [3,5,6,7,9,8,5,3,2,87,564,23,90]
# b = []
# for item in a:
#     if item%2 == 0:
#         b.append(item)
# print(b)

# ## 2 
# a = [3,5,6,7,9,8,5,3,2,87,564,23,90]
# b = [i for i in a if i%2==0] # here i means item in a and it print the number that is divisibel by 2 in list
# print(b)


## for set comprehension
t = [1,3,4,6,4,3,2,1,6]
# s = {i for i in t}  # it does not print repeated value
# print(s)

# ###
s = set(t)
print(s)