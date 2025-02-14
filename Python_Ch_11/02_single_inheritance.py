class Employee:
    company = "Google"

    def showDetails(self):
        print("This is employee")

class Programmer(Employee):
    language = "Pyhton"
    # company = "Youtube"   ## here google is printed if this line does not execute

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is a programmer")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)