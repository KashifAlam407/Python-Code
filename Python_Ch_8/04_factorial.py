# n! = 1 * 2 * 3 * 4....*n
# n! = [1 * 2 * 3 * 4.. n-1]*n
# n! = n * (n-1)!


### 1
# n = 0 
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)


### 2
# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product

# f = factorial_iter(5)
# print(f)

### 3
 
# def factorial_iter(n):   
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product

#### 4
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)     ## factorial(0-1) = -1 and -1 multiplied to n then negative value, why not?

f = factorial(4)
print(f)

#### 5
# class Solution():
#     def __init___(self, k, x):
#         self.k = k
#         self.x = x
# for i in range(2,20):
#     i = i + (i-2)
#     if i > 20:
#         print("Voldemart has been died in {i} steps")
#     break
        
# p = Solution(2, 20)
# print(p)


# class Solution:
#     def minimumAttacks(self, X, K):
#         for i in range(2,20,2):
#             j = (i + (i-2))
            
#             if j > 20:
#                 print(f"Voldemart has been died in {i} steps")
#                 break
            
            
        
    
        
            
# p = Solution()
# p.minimumAttacks(2, 20)

