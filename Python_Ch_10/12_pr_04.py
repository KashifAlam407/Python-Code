class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The square of {self.number} is {self.number**2}")

    def squareRoot(self):
        print(F"The squre root of {self.number} is {self.number**0.5}")

    def cube(self):
        print(f"The cube of {self.number} is {self.number**3}")

    def cubeRoot(self):
        print(f"The cube root of {self.number} is {self.number**(1/3)}")

    @staticmethod
    def greet():
        print("Hello there! Welcome to the best Calculator of the World")

a = Calculator(8)
a.square()
a.squareRoot()
a.cube()
a.cubeRoot()
a.greet()