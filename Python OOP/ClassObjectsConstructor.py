class Automobile:
    def __init__(self, model, year, type):
        self.model = model
        self.year = year
        self.type = type

#above is the template kind of class, where we don't need to declare everytime


Civic = Automobile(model="Civic", year="2007", type="Sedan") #we just need to add values and can be done two ways

Alto = Automobile("Alto LXI", 2019, "Hatchback" ) 

print(Civic.model, Alto.year)