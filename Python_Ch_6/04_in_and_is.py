a = None
if (a is None):
    print("Yes")
else:
    print("No")


#### Using 'in' and 'is' operators in Python
# The 'in' operator checks for membership in a sequence (like lists, tuples, strings).
# The 'not in' operator checks if a value is not present in a sequence.
# The 'is' operator checks for identity, i.e., whether two variables point to the same object in memory.
# The 'is not' operator checks if two variables do not point to the same object in memory.



a = [45, 56,67]

print(45 in a)  # returns true because 45 is in list
print(456 in a)  # returns false because 456 is not in list
print(45 not in a)  # returns false because 45 is in list
print(456 not in a)  # returns true because 456 is not in list
print(45 is a)  # returns false because 45 is not the same object as a 
print(45 is not a)  # returns true because 45 is not the same object as a
