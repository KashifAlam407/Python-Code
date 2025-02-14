f = open("sample.txt")

data = f.readline()  # for 1st line
print(data,end="")  # by default \n


data = f.readline()  # for 2nd line
print(data,end="")   # by default \n


data = f.readline()  # for 3rd line
print(data)


data = f.readline()  # for 4th line
print(data)
f.close()