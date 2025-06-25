a = "Kashif's"
b = 'Kashif"s'
c = '''Kashif"s and Kashif's'''
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))


s = "Kashif"
# print(s[5: -5]) # This will print an empty string because the start index is greater than the end index
print(s[3:-1])  # This will print 'hi' (from index 3 to the second last index)
print(s[-5: 5])  # This will print 'ashi' (from index -5 to index 5, which is the entire string)
print(s[5:-5:-1])


print(s[0:5:2])  # This will print 'Ksf' (from index 0 to index 5 with a step of 2)
print(s[0:5:-2])  # This will print an empty string because the step is negative and the start index is less than the end index