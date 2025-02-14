class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod    ### When a method doesn’t need access to instance data (no self parameter used), it can be defined as a static method
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

harry = Employee()
harry.salary = 100000
# Employee.salary() = 100000    ## throws an error since it not a static method
harry.getSalary("Thanks")  # Employee.getSalary(harry)
harry.greet()  # Employee.greet()
Employee.greet()
harry.time()
# kashif = Employee()
# kashif.greet()

