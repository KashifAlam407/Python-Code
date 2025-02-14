class Employee:
    company = "Google"

harry = Employee()
rajni = Employee()
print(harry.company)  # print(Employee.company) also work
print(rajni.company)
Employee.company = "YouTube"
print(harry.company)
print(rajni.company)