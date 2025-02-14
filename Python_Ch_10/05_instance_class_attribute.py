class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
harry.salary = 300
rajni.salary = 400

harry.salary = 45  ## printed because it is latest
rajni.salary = 40

Employee.salary = 10  ## Not executed when the 9,10,12 and 13 line is executed but why???


print(harry.salary)
print(rajni.salary)

## Below line throws an error as address is not present in instance/class
# print(rajni.address)