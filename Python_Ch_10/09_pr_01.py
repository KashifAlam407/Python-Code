class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")

kashif = Programmer("Kashif", "Skype")
alka = Programmer("Alka", "Github")
kashif.getInfo()
alka.getInfo()