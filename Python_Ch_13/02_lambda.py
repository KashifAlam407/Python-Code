# def func(a):
#     return a+5

func = lambda a: a+5  ## here the value of a is comes from x
square = lambda x: x*x
sum = lambda a,b,c: a+b+c

x = 3 
print(func(x))
print(square(x))
print(sum(x, 2, 4))




###### Lambda with list
li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())
