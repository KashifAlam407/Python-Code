# syntax:

# split(seperator, maxsplit)

# The delimiter string on which the split will occur. If not specified, any whitespace is used
# The maximum number of splits to perform. The default value, -1, means "all occurrences.



words = input("Enter: ").split()
print(words)

# Output:
# Enter: kashif alam ashif alam khan
# ['kashif', 'alam', 'ashif', 'alam', 'khan']



#  To split a number (typically an integer or float) into its individual digits, you can convert the number to a string and then split the string. Here’s an example:
name = "kashif"
num = "kashif", "ashif", "alam"
numa = "kashif alam khan"
number = 123456
digits = list(str(number))
print(list(name))
print(list(num))
print(list(numa))
print(digits)

# Output:
# ['k', 'a', 's', 'h', 'i', 'f']
# ['kashif', 'ashif', 'alam']
# ['k', 'a', 's', 'h', 'i', 'f', ' ', 'a', 'l', 'a', 'm', ' ', 'k', 'h', 'a', 'n']
# ['1', '2', '3', '4', '5', '6']






###### Use of separator/delimeter

string = "one,two,three"
words = string.split(',')   ## ','(separator)separate kaha karna hai
print(words)

# Output:
# ['one', 'two', 'three']




text = 'geeks for geeks'
print(text.split())    ## splitting at whitespalce (since whitespace is default)

# Output:
# ['geeks', 'for', 'geeks']



word = 'geeks, for, geeks'
print(word.split(','))   ## splitting at ,

# Output:
# ['geeks', ' for', ' geeks']




word = 'geeks:for:geeks'
print(word.split(':'))   ## splitting at :

# Output:
# ['geeks', 'for', 'geeks']




word = "CatBatSatFatOr"
print(word.split('t'))   ## splitting at t

# Output:
# ['Ca', 'Ba', 'Sa', 'Fa', 'Or']




##### Use of maxsplit

word = "geeks, for, geeks, kashif"
print(word.split(',', 0))   ## here 0 is maxsplit (string ka substring kitne banenge )
print(word.split(',', 1))
print(word.split(',', 2))
print(word.split(',', 3))
print(word.split(',', 4))

# Output:
# ['geeks, for, geeks, kashif']
# ['geeks', ' for, geeks, kashif']
# ['geeks', ' for', ' geeks, kashif']
# ['geeks', ' for', ' geeks', ' kashif']
# ['geeks', ' for', ' geeks', ' kashif']




multiline_text = "Line 1\nLine 2\nLine 3"
lines = multiline_text.split('\n')
print(lines)  

# Output:
# ['Line 1', 'Line 2', 'Line 3']