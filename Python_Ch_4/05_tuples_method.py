# Creatig a tuple using ()
t = (1, 2, 4, 5, 32, 2, 12)
# print(t)
for x in t:
    print(x)


print(t.count(2))   ## prints the number of occurence of 2
print(t.index(5))    ## prints the value of index 5


#### ================ =============== ================
tup = (((1,2,3), (4,5,6)), ((7,8,9), (10,11,12)), ((233,54,23), (14,15,18)))
# print(tup[0][1][2])  # Accessing nested tuple elements
for x in tup:
    for y in x:
        for z in y:
            print(z)

print(tup[1][1][2])

z = tuple([num for num in tup for j in num for k in j])
print(z)  # Flattening the nested tuple into a single tuple
# Using tuple comprehension to flatten a nested tuple
# Note: Tuple comprehension is not a built-in feature in Python, but we can use a generator expression to achieve similar results.
# Using a generator expression to flatten a nested tuple
def flatten_tuple(nested_tuple):
    for item in nested_tuple:
        if isinstance(item, tuple):
            yield from flatten_tuple(item)
        else:
            yield item


#### Unpacking a tuple with disposable variable(_)
person = ("Kashif", 21, "Alam", "Md")
name, age, _, _ = person 
print(name)
print(age)



### Shallow Copying a Tuple
# Shallow copying a tuple with mutable elements
t1 = (1, 2, [3, 4, 5], 6, 7)
t2 = t1[:] # Copying a tuple
t2[2].append(8)  # Modifying the list inside the tuple
print(t1)  # Original tuple also changed
print(t2)  # Copied tuple reflects the change



import copy
# Deep copying a tuple with mutable elements
t3 = (1, 2, [3, 4, 5], 6, 7)
t4 = copy.deepcopy(t3)  # Deep copying the tuple
t4[2].append(8)  # Modifying the list inside the tuple  
print(t3)  # Original tuple remains unchanged
print(t4)  # Copied tuple reflects the change
# Note: Tuples are immutable, but if they contain mutable elements (like lists), those elements can be modified.

print(t3+t4)  # Concatenating tuples
# Using the + operator to concatenate tuples



#####
num = (2, 3, 4, 5, 3, 5, 3, 15, 20)

is_divisible = any(n % 5 == 0 for n in num)
print(is_divisible)  # True if any number in the tuple is divisible by 5, otherwise False
all_divisible = all(n % 5 == 0 for n in num)    
print(all_divisible)  # True if all numbers in the tuple are divisible by 5, otherwise False
# Using any() and all() to check divisibility by 5 in a tuple
# Using the map() function to apply a function to each element in a tuple


#### Class work 
##########   Ques 1   ################
data = ('Python', 3.10, 2025, ('AI', 'ML', ('DL', 'NLP')), True)

# print(data[3][2][1])

# py, versioin, year, _, _, = data
# print(py)  # Output: Python
# print(versioin)  # Output: 3.10
# print(year)  # Output: 2025


# import copy
# data2 = copy.deepcopy(data)  # Deep copying the tuple
data3 = list(data)
# print(data3[3][1])
data3[3][1] = 'Prompt Engineering' # Modifying the nested tuple
print(data3)  # Output: ('Python', 3.10, 2025, ('AI', 'Prompt Engineering', ('DL', 'NLP')), True)
# print(data2)  # Original tuple remains unchanged
print(data)


# data.append("Finished")  # Attempting to append to a tuple will raise an error


###############  Ques 2   #################
x = ('hello')
y = ('hello',)

print(type(x))  # Output: <class 'str'>
print(type(y))  # Output: <class 'tuple'>

z = list(y)  # Converting tuple to list
print(z)  # Output: ['hello']
z[0] = 'Hello'
print(z)

z = tuple(z)  # Converting list back to tuple
print(z)  # Output: ('Hello',)
print(type(z))  # Output: <class 'tuple'>
# Converting a tuple to a list and back to a tuple
# print(type(tuple(z)))