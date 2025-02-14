## python return statement

def add(a,b):
    return a+b  ## returning sum of a and b

def is_true(a):
    return bool(a)  ## returning a boolean value

sum = add(5,4)   ## calling the add() with parameter
print(sum)

res = is_true(-3)  ## function call
print(res)   ## true is printed since non zero number means true and zero means false





####  When the return statement is executed, the function terminates and the specified value is returned to the caller. If no value is specified, the function returns None by default.

####  Return statement can not used outside the function




## Returning Mulitiple Values
def fun():
    first_Name = "Kashif"
    last_Name = "Alam"
    return first_Name, last_Name

name1, name2  = fun()   ## first_Name is stored in name1 and last_Name is stored in name2 
print(name1)
print(name2)
    


## Returning List
def fun(n):
    return [n**2, n**3]

res = fun(3)
print(res)



## Function returning another function
def fun1(msg):
    def fun2():
        return (f"Message: {msg}")   ## Using the outer function's message
    return fun2

fun3 = fun1("Hello, World!")   ## Getting the inner function

print(fun3())   ## calling the inner function



