class Employee:
    company = "Google"
    salary = 1000
    location = "Delhi"

    # def changeSalary(self, sal):   ## It is used to add a new salary to the class salary  (sal is instance attribute)
    #     self.__class__.salary = sal   ## this method is also known as dunder method 
      
    @classmethod    ## It is used to change class attribute (decorator), it can change the class variable of class
    def change(cls, sal, loc): 
        cls.salary = sal    ## you can change anything in the class attribute by typing the class varible and to eccess the class
        cls.location = loc

e = Employee()
print(e.salary)
e.change(455, "lucknow")
# Employee.salary = 67    ## It can also change the class salary
# print(Employee.salary)
print(e.salary)
print(e.location)
print(Employee.salary)