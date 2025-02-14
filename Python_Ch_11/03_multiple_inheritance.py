class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradelevel(self):
        self.level = self.level + 1
        
class Employee:
    company = "Visa"
    eCode = 120

class Programmer(Freelancer, Employee):
    name = "Rohit"

p = Programmer()
p.upgradelevel()
print(p.company)   ## Fiverr is printed because at first Freelancer is call in "class Programmer"
# print(p.upgradelevel)   ## Think