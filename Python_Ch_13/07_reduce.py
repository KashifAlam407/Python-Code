from functools import reduce

sum = lambda a,b: a+b

l = [1,2,3,4,5,6]

# sum = l[0] + l[1]   ## it gives error if executed

val = reduce(sum, l)
print(val)



#### Rough
# l = [1,2,3,4,5,6]
# print(lambda l: l[0] + l[1])