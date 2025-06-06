

## 1. if-elif-else ladder in python
a = 8
if(a>12):
    print("The value of a is grater than 12")
elif(a>13):
    print("The value of a is greater than 13")
elif(a>7):
    print("The value of a is grater than 7")
elif(a>17):
    print("The value of a is grater than 17")
else:
    print("The value of a is grater than 3 or 7")


# 2. Multiple if statesment
a = 8
if(a>12):
    print("The value of a is grater than 12")
if(a>3):
    print("The value of a is greater than 3")
if(a>7):
    print("The value of a is grater than 7")
if(a>17):
    print("The value of a is grater than 17")
else:
    print("The value of a is grater than 3 or 7")
print("Done")


b = 22
if(b>9):
    print("Greater")
else:
    print("Lesser")


# 3. Nested if statement
if(b>9):
    print("Greater")
    if(b>20):
        print("Greater than 20")
    else:
        print("Lesser than 20")
else:
    print("Lesser")
    if(b<5):
        print("Lesser than 5")
    else:
        print("Greater than 5")


#-----------------------------------------
#---- Advanced if statements in Python ----
# ----------------------------------------

# 4. Ternary operator
c = 5
d = 10 if c > 5 else 20
print(d)  # This will print 20 because c is not greater than 5


# 5. One-liner if-else statement
e = 15
print("Greater than 10") if e > 10 else print("Lesser than or equal to 10")



# 6. Using 'and' and 'or' in if statements
f = 12
if f > 10 and f < 20:
    print("f is between 10 and 20")
if f < 10 or f > 20:
    print("f is either less than 10 or greater than 20")


# 7. Using 'not' in if statements
g = 5
if not g > 10:
    print("g is not greater than 10")



# 8. Using 'in' operator in if statements
h = [1, 2, 3, 4, 5]
if 3 in h:
    print("3 is in the list h")


# 9. Using 'is' operator in if statements
i = [1, 2, 3]
j = i
if i is j:
    print("i and j are the same object in memory")
print(i)
print(j)


# 10. Using 'is not' operator in if statements
k = [1, 2, 3]
l = [1, 2, 3]
if k is not l:
    print("k and l are not the same object in memory")

print(id(k))  # This will print the memory address of k
print(id(l))  # This will print the memory address of l


# 11. Using 'if' with a function
def check_value(x):
    if x > 10:
        return "x is greater than 10"
    else:
        return "x is less than or equal to 10"
    
result = check_value(15)
print(result)  # This will print "x is greater than 10"



# 12. Using 'if' with a list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers if x > 2]
print(squared_numbers)  # This will print [9, 16, 25] because only numbers greater than 2 are squared


# 13. Using 'if' with a dictionary comprehension
numbers_dict = {x: x**2 for x in range(1, 6) if x > 2}
print(numbers_dict)  # This will print {3: 9, 4: 16, 5: 25} because only numbers greater than 2 are included in the dictionary  


# 14. Using 'if' with a set comprehension
numbers_set = {x**2 for x in range(1, 6) if x > 2}
print(numbers_set)  # This will print {9, 16, 25} because only numbers greater than 2 are squared and included in the set


# 15. Using 'if' with a generator expression
numbers_gen = (x**2 for x in range(1, 6) if x > 2)
for num in numbers_gen:
    print(num)  # This will print 9, 16, 25 because only numbers greater than 2 are squared and yielded by the generator expression


# 16. Using 'if' with a while loop
count = 0
while count < 5:
    if count % 2 == 0:
        print(f"{count} is even")
    else:
        print(f"{count} is odd")
    count += 1  # Increment the count to avoid infinite loop


# 17. Using 'if' with a for loop
for num in range(1, 6):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")  # This will print whether each number from 1 to 5 is even or odd


# 18. Using 'if' with a try-except block
try:
    x = int(input("Enter a number: "))
    if x > 10:
        print("x is greater than 10")
    else:
        print("x is less than or equal to 10")
except ValueError:
    print("Please enter a valid integer")


# 19. Using 'if' with a function that returns a boolean
def is_even(num):
    return num % 2 == 0

def check_evenness(x):
    if is_even(x):
        return f"{x} is even"
    else:
        return f"{x} is odd"
    
result = check_evenness(8)
print(result)  # This will print "8 is even"


# 20. Using 'if' with a lambda function
is_positive = lambda x: x > 0
def check_positive(x):
    if is_positive(x):
        return f"{x} is positive"
    else:
        return f"{x} is not positive"
    
result = check_positive(-5)
print(result)  # This will print "-5 is not positive"



# 21. Using 'if' with a class method
class Number:
    def __init__(self, value):
        self.value = value

    def check_value(self):
        if self.value > 10:
            return f"{self.value} is greater than 10"
        else:
            return f"{self.value} is less than or equal to 10"
        
num = Number(12)
print(num.check_value())  # This will print "12 is greater than 10"



# 22. Using 'if' with a class method and a static method
class Number:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def is_even(num):
        return num % 2 == 0

    def check_value(self):
        if self.value > 10:
            return f"{self.value} is greater than 10"
        else:
            return f"{self.value} is less than or equal to 10"
        
num = Number(8)
print(num.check_value())  # This will print "8 is less than or equal to 10"

print(num.value)
print(num.is_even(num.value))  # Using the static method to check if the number is even, i'm calling it using the class instance
print(Number.is_even(num.value))  # This will print True because 8 is even, and I'm calling the static method using the class name




# 23. Using 'if' with a class method and a class variable
class Number:
    count = 0  # Class variable to keep track of the number of instances

    def __init__(self, value):
        self.value = value
        Number.count += 1  # Increment the class variable when a new instance is created

    @classmethod
    def get_count(cls):
        return cls.count  # Return the current count of instances

    def check_value(self):
        if self.value > 10:
            return f"{self.value} is greater than 10"
        else:
            return f"{self.value} is less than or equal to 10"
        
num1 = Number(12)
num2 = Number(8)
print(num1.check_value())  # This will print "12 is greater than 10"
print(num2.check_value())  # This will print "8 is less than or equal to 10"
print(Number.get_count())  # This will print 2 because two instances of the Number class have been created



# 24. Using 'if' with a class method and inheritance
class Number:
    def __init__(self, value):
        self.value = value

    def check_value(self):
        if self.value > 10:
            return f"{self.value} is greater than 10"
        else:
            return f"{self.value} is less than or equal to 10"
        
class EvenNumber(Number):
    def is_even(self):
        return self.value % 2 == 0  # Check if the number is even
class OddNumber(Number):
    def is_odd(self):
        return self.value % 2 != 0  # Check if the number is odd
    
num = EvenNumber(8)
print(num.check_value())  # This will print "8 is less than or equal to 10"
print(num.is_even())  # This will print True because 8 is even
num2 = OddNumber(7)
print(num2.check_value())  # This will print "7 is less than or equal to 10"
print(num2.is_odd())  # This will print True because 7 is odd




# 25. Using 'if' with a class method and multiple inheritance
class Number:
    def __init__(self, value):
        self.value = value

    def check_value(self):
        if self.value > 10:
            return f"{self.value} is greater than 10"
        else:
            return f"{self.value} is less than or equal to 10"
        
class EvenNumber(Number):
    def is_even(self):
        return self.value % 2 == 0  # Check if the number is even
    
class OddNumber(Number):
    def is_odd(self):
        return self.value % 2 != 0  # Check if the number is odd
    
# Example of using the classes
num = EvenNumber(8)
print(num.check_value())  # This will print "8 is less than or equal to 10"
print(num.is_even())  # This will print True because 8 is even

num2 = OddNumber(7)
print(num2.check_value())  # This will print "7 is less than or equal to 10"
print(num2.is_odd())  # This will print True because 7 is odd




# 26. Using 'if' with a class method and class attributes


