# num = int(input("Enter the number: "))
# sum = 0
# for i in range(num+1):
#     sum = sum + i 

# print(sum)


num = int(input("Enter the number: "))
sum = 0
for i in range(2,num+1,2):
    sum = sum + i 
    if sum > 30:
        print(f"Villain died in {i/2} steps")
        break

# print(sum)
    
