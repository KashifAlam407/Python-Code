######### 1
class Car:
    def __init__(self, brand, model):
        self.brand = brand   ## set instance attribute
        self.model = model  ## set instance attribute

    def display(self):
        # return self.brand, self.model
        return (f"This car is {self.model}, build by {self.brand}")

    
## Create an instance of Car
car1 = Car("Toyota", "Carolla")

## Call the display method
print(car1.display())  



######## 2
class boy:
    def __init__(self, subject):
        self.subject = subject

    def read(self):
        print("Topic", self.subject)

ins = boy("Kashif")

ins.read()