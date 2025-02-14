class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):    ### a constructor is a special method that is automatically called when an object of a class is instantiated
        self.name = name 
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
        
    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

harry = Employee("Harry", 100, "Youtube")
# harry = Employee()  ---> This throws an error (missing 3 required positional arguments:)
harry.getDetails()
# harry.getSalary("Thanks")
# harry.time()