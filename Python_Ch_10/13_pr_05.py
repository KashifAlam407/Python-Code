class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print('**************')
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print('**************')

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats)>0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = (self.seats)-1
        else:
            print("Sorry this train has been full! Kindly try in tatkal")
    
    def cancelTicket(self):
        if(self.seats)==0:     ## do yourself implement canceled ticket
            print("Your Ticket has been canceled because all the seats are booked already")

intercity = Train("Intercity Express: 14987", 90, 2)
intercity.getStatus()
intercity.bookTicket()
intercity.cancelTicket()   ## if seat == 0 then cancel ticket
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket()   ## Ticket canceled because all the seats are booked