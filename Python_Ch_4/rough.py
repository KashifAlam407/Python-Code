# Great!! No need to use sort and n2=n1.
n = [1,1,2,3,4,4,4,5,5,5,6,6,6]
#n.sort()
n1 = set(n)
n1.remove(max(n))
# n2 = n1
print(f' The Runnerup value is {max(n1)}')


## 2
# n = [1,1,2,3,4,4,4,5,5,5,6,6,6]
# n.sort()
# print(n[n.index(max(n))-1])

### w
n = [1,1,2,3,4,4,4,5,5,5,6,6,6]
n.sort()
a = set(n)
print(len(a)-1)


### w
# n = [1,1,2,3,4,4,4,5,5,5,6,6,6]
n = [4,4,4,-4]
n.sort()
a = (max(n))
print(n.index(a)-1)
print[0]
