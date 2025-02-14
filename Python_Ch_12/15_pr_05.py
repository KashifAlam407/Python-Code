num = int(input("Enter your number: "))
table = [num*i for i in range(1,11)]
print(table)    

with open("Table.txt", "a") as f:
    f.write(str(table))   ## here we write str because write aurgument must be str not list 
    f.write("\n")