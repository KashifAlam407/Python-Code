## Creating an empty set
b = set()
print(type(b))

# Adding value to an empty set
b.add(4)
b.add(5)
b.add(5)  ## Adding a value repetedly does not change a set
b.add(4)
# b.add([3,5,12,8])   ## you can not add list in set because list is mutable(can change)
b.add((3,5,12,8))    ## you can add tuple in a set because tuple is immutable(cannot change)
# b.add({3:9})   ## you can not add dictionary in set because dictionary is mutable(can change)
print(b)

## Removing of an item
print(len(b))  ## prints the length of this set
b.remove(4)  ## removes 4 from set b
# b.remove(34)   ## throws an error
print(b)

print(b.pop()) ## Removes an arbitrary element from the set and return the element removed
print(b)

b.clear()  ## clear the set
print(b)


b = {1, 2, 3, 4, 5}
print(b)

b.discard(3)  ## removes 3 from set b, does not throw an error if 3 is not present
print(b)

b.discard(10)  ## does not throw an error if 10 is not present
print(b)


b = {1, 2, 3, 4, 5}
b.remove(2)  ## removes 2 from set b, throws an error if 2 is not present
print(b)


b = {1, 2, 3, 4, 5}
b.pop()  ## removes an arbitrary element from the set and return the element removed
print(b)


# Creating an empty set
b = {1, 2, 3, 4, 5}
b.clear()  ## clears the set
print(b)  ## prints an empty set


# Adding elements to a set
b = {1, 2, 3, 4, 5}
b.add(6)  ## adds 6 to set b
b.add(7)  ## adds 7 to set b
print(b)  ## prints the set with added elements


# Removing elements from a set
b = {1, 2, 3, 4, 5}
b.remove(3)  ## removes 3 from set b, throws an error if 3 is not present
print(b)  ## prints the set after removing 3


# Creating a set with a tuple
b = {1, 2, 3, 4, 5}
b.add((6, 7))  ## adds a tuple (6, 7) to the set
print(b)  ## prints the set with the added tuple


# Adding a frozenset to a set
b = {1, 2, 3, 4, 5}
b.add(frozenset([6, 7]))  ## adds a frozenset to the set
print(b)  ## prints the set with the added frozenset


# Adding a dictionary to a set
b = {1, 2, 3, 4, 5}
# b.add({'a': 1, 'b': 2})  ## throws an error because you cannot add a dictionary to a set


# Adding a list to a set
b = {1, 2, 3, 4, 5}
# b.add([6, 7])  ## throws an error because you cannot add a list to a set


# Adding a number to a set
b = {1, 2, 3, 4, 5}
b.add(6)  ## adds 6 to set b
print(b)  ## prints the set with the added number


# Adding a tuple to a set
b = {1, 2, 3, 4, 5}
b.add((6, 7))  ## adds a tuple (6, 7) to the set
print(b)  ## prints the set with the added tuple


# Adding a string to a set
b = {1, 2, 3, 4, 5}
b.add("Hello")  ## adds a string "Hello" to the set
print(b)  ## prints the set with the added string


# Adding a boolean to a set
b = {1, 2, 3, 4, 5}
b.add(True)  ## adds a boolean True to the set
print(b)  ## prints the set with the added boolean


# Adding a float to a set
b = {1, 2, 3, 4, 5}
b.add(3.14)  ## adds a float 3.14 to the set
print(b)  ## prints the set with the added float



# Adding a complex number to a set
b = {1, 2, 3, 4, 5}
b.add(2 + 3j)  ## adds a complex number 2 + 3j to the set
print(b)  ## prints the set with the added complex number



# Adding a range to a set
b = {1, 2, 3, 4, 5}
b.update(range(6, 11))  ## adds a range of numbers from 6 to 10 to the set
print(b)  ## prints the set with the added range



# Adding multiple elements to a set
b = {1, 2, 3, 4, 5}
b.update([6, 7, 8])  ## adds multiple elements 6, 7, and 8 to the set
print(b)  ## prints the set with the added elements


# Adding a set to another set
b = {1, 2, 3, 4, 5}
c = {6, 7, 8}
b.update(c)  ## adds all elements of set c to set b
print(b)  ## prints the set with the added elements from set c



