class Employee:
    company = "Google"
    salary = 5600
    salarybonus = 400
    # totalSalary = salary + salarybonus
            
    @property   ## this method is also known as getter 
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter   ## this method is also known as setter method
    def totalSalary(self, val):   ## it takes value from line no. 17, it change the salary bonus according to total salary
        self.salarybonus = val - self.salary
        

e = Employee()
print(e.totalSalary)   ## here totalSalary is a property that's why i can't call it like this totalSalary()
# e.totalSalary(6800)   ## throws an error 
e.totalSalary = 6800
print(e.salary)
print(e.salarybonus)   ## here salarybonus is a property that's why i can't call it like this salaybonus()
