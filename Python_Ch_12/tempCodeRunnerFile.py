noprimes = [j for i in range(2, 50) for j in range(i*2, 50, i)]  
primes = [x for x in range(2, 50) if x not in noprimes]  
print (primes)  
print(noprimes)