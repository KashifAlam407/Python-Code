# import pandas as pd
# pd.DataFrame()

class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

kashif = RailwayForm()
kashif.name = "Kashif" 
kashif.train = "T Expresss"        
kashif.printData()