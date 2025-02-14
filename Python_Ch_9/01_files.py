## use open function to read the content of a file!

f = open("sample.txt", 'r')
# f = open("sample.txt")  # by default the mode is r
read = f.read()
print(read)
f.close()

# f = open("sample.txt")  # by default the mode is r
# text = f.read(6)  # read only firt 6 character
# print(text)
# f.close()
