#               ---- MADE BY MD KASHIF ALAM ----

n = int(input("Enter the number of rows: "))
name = input("Enter the name: ")
m = n//2
k = len(name)
for i in range(m):        # for 1st part
    for j in range(m-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="") 
    
    if n % 2 == 0:                 # for 2nd part
        for j in range(2*(m-i-1)):
            print(" ",end="")
    else:
        for j in range(2*(m-i-1)+2):
            print(" ",end="")
    for j in range(i+1):
        print("* ",end="")  

    print()

# print = ("* " * ((n-k)//2) + " ".join(name) + " *" * ((n-k)//2))    # it is for name print inside the heart
                                                                      # this is not true for all value so, it is given in 26 line 
if n % 2 == 0:
    if k % 2 == 0:
        print("* " * ((n-k)//2) + " ".join(name) + " *" * ((n-k)//2))  # for name inside the heart
    else:
        print("* " * ((n-k)//2) + " ".join(name) + " *" * ((n-k)//2)+1)
else:
    if k % 2 == 0:
        print("* " * ((n-k)//2) + " ".join(name) + " *" * ((n-k)//2)+1)  
    else:
        print("* " * ((n-k)//2) + " ".join(name) + " *" * ((n-k)//2))


for i in range(n,0,-1):  # for 3rd part
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("* ",end="")
    print()
    




    
