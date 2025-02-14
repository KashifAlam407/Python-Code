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