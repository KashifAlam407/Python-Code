a = 4
b = 5

# a = a & b
a &= b

# Output
print(a)



#################################
# a list
a = [1, 2, 3, 4, 5]

# walrus operator
while(x := len(a)) > 2:     ## walrus operator used to assigen value in an expression
    a.pop()
    print(x)


#########################

def fun(*args):
    # Concatenate all arguments
    result = " ".join(args)
    print(result)

# Function calls
fun("Geeks", "forGeeks", "kashif", "alam")



##########################

def f():
    print(s)  # Line 1   ## Throws an error since no variable named s (variable create hone se pahle print nahi kar sakte)

    s = "Me too."  # Line 2   ## ab iss function me global variable(s) access nahi ho sakta (this is shadow of global s)

    print(s)  # Line 3  ## it prints "Me too."

# Global scope
s = "I love Geeksforgeeks"
f()
print(s)


#################################

def fun():
    name = "Alice"
    age = 30
    return name, age

name, age = fun()   ## the returned value form line(54) name, age is stored in name, age respectively in line(56)

print(name)  
print(age) 












