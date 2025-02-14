class Sample:
    def __init__(self, name):   ## you can write any thing on the place of self but it is difficult for another programmer to understand 
        self.name = name

obj = Sample("Kashif")
print(obj.name)