class company:
    salary = 3400
    employee = 45
    lab = 2

    def showsalary(self,):  ## here all functions are method
        print(self.salary)

    def showemployee(self):   ## self is a argument 
        print(self.employee)

    def showlab(self):
        print(self.lab)

    def __init__(self):   ## no need of function call (executed when the object is defined)
        print("Hii Dear")

    def add(self,p,q):     ## p and q are argument 
        print(p+q)



a = company() ## object
a.showsalary()   ## function call
a.showemployee()
a.showlab()
a.add(23,32)   ## here argument is passing 
