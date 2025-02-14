# to chech whwther 2 files are identical or not 
## 1

with open("copy.txt") as f:
    a = f.read()

with open("this.txt") as f:
    b = f.read()

if a == b:
    print("Files are identical")

else:
    print("Files are not identical")



## 2
# file1 = "copy.txt"
# file2 = "this.txt"

# with open(file1) as f:
#     f1 = f.read()

# with open(file2) as f:
#     f2 = f.read()

# if f1 == f2:
#     print("Files are identical")
# else:
#     print("Files are not identical")