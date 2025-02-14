for i in range(10):
    print(i)
else:
    print("This is inside else of for")





###########################
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index], end=" ")

###########################
string = ["geeks", "for", "geeks"]
char = [i for i in string]
print(char)



##########################################
# python code to demonstrate working of items()

king = {'Ashoka': 'The Great', 'Chandragupta': 'The Maurya',
		'Modi': 'The Changer'}

# # using items to print the dictionary key-value pair
for key, value in king.items():
	print(key, value)

print(king.items())



#################################33
# Prints all letters except 'e' and 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    
    print('Current Letter :', a[i])
    i += 1
