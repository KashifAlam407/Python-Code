greeting = "Good Morning, "
name = "Kashif"
# print(type(name))
c = greeting + name
print(c)
print(name[3])  # gives the index of the name variable
# name[3] = "dgf" # does not work
print(name[0:4])  # string slicing
print(name[:4])
print(name[0:])
print(name[0:-1])
print(name[-1])
print(name[-6:-1])   ## here index -6 is equal to index 0
print(name[-6:])
print(name[-6:6])

## string slicing with skip value
name = "kashifIsAGoodBoy"
print(name[0:12:1])  ## it does not skip the value
print(name[0:12:2])   ## it skip 1 value
print(name[0::2])