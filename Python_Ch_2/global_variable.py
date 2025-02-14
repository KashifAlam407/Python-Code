###
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()



# ###
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)




# ## 
x = "awesome"

def myfunc():
  global x      ## it means variable x is globally 
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# x = 5
# y = "John"
# print(x + y)
