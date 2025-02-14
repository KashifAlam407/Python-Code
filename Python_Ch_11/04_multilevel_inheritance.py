class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am Employee so i am luckily breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers..")
    
    def takeBreath(self):
        print("I am a Programmer so i am breathing++..")

p = Person()     ## object
p.takeBreath()    ## function call
# print(p.company) # throws an error

e = Employee()     ## object
e.takeBreath()     ## function call
print(e.company)

pr = Programmer()   ## object
pr.takeBreath()    ## function call
print(pr.company)    
print(pr.country)