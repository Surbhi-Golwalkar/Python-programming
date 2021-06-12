# Write a class Train which has methods to book a ticket, 
# get status(no of seats) 
# and get fare information of trains running under Indian Railways.

class train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("************************")
        print(f"The name of train is {self.name}")
        print(f"The seats availaible in train are {self.seats}")

    
        