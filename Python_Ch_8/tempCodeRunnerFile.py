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
# print(d["add"](5, 3))
print(d["add"])
print(d["subtract"](5, 3))