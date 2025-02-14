## salaryAfterIncrement = salary * increment

class Employee:
    salary = 2000
    increment = 1.5
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter         ## You can also take result without this function
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement = 4000
print(e.increment)

    

    