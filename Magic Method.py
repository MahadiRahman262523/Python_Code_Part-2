class Bike :
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour

    def __eq__(self, other):
         return self.name == other.name and self.colour == other.colour

    def __str__(self):
        return(f"Name : {self.name},Colour : {self.colour}")

    def display(self):
        print(f"Name : {self.name},Colour : {self.colour}")



b1 = Bike("Yamaha R15","Blue")
b2 = Bike("Yamaha R15","Blue")
print(b1)
print(b2)
print(b1==b2)