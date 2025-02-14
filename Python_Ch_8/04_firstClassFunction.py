#### Asssigned to Variables
def msg(name):
    return f"Hello, {name}!"

## Assigning the function to a variable 
f = msg

## Calling the function using the variable
print(f("Kashif"))



#----------------------------------------
#### Passing functions as Arguments
def msg(name):
    return f"Hello, {name}!"


def fun1(fun2, name):
    return fun2(name)   ### here fun2 is equal to msg

## passing the greet function as an argument
print(fun1(msg, "Bob"))



#--------------------------------------
#### Returning function from other functions
def fun1(msg):
    def fun2():
        return f"Message: {msg}"
    return fun2

## Getting the inner function
func = fun1("Hello, World!")
print(func())



#---------------------------------------
#### Storing functions in Data Structures
def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

## storing function in a dictionary 
d = {
    "add": add,     ## whenever the "add"(key) is called the add(value) function is called automatically
    "subtract": subtract
}

## calling functions from the dictionary
# print(d["add"])    ## corresponding value of add(key) is called present in dictionary(d)
print(d["add"](5, 3))
print(d["subtract"](5, 3))