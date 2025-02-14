## 1
class Employee:
    company = "Google"
    def getSalary(self): 
        print("Salary is 100k")

harry = Employee()
harry.getSalary()  # Employee.getSalary(harry)




## 2  
class Employee:
    company = "Google"
    def getSalary(self):  ## here self means jiski baat ki ja rahi hai example harry and kashif
        print(f"Salary for this employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 1000
harry.getSalary()  # Employee.getSalary(harry)
kashif = Employee()
kashif.salary = 1999
kashif.getSalary()




## 3
class Employee:
    company = "Google"
    def getSalary(harry):
        print(f"Salary for this employee working in {harry.company} is {harry.salary}")    ## here formatting is done 

harry = Employee()
harry.salary = 100000
harry.getSalary()  # Employee.getSalary(harry)
kashif = Employee()   
kashif.salary = 343430
kashif.getSalary()

