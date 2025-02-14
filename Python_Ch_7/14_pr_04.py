# To check where a no. is prime or not prime

num = int(input("Enter the number: "))
prime = True
for i in range(2, num):  # here 2 is written because the given no. is devided form 2 to the given no.
    if(num%i == 0):  # if true then prime is false
        prime = False
        break  # if we do not write break function here then programm also execute but we have to write 
    
if prime:
    print("This number is Prime")
else:
    print("This number is not prime")
