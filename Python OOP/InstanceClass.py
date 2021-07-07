class Automobile:
    
    Time = 3
    
    def __init__(self, model, year, type):
        self.model = model
        self.year = year
        self.type = type

#above is the template kind of class, where we don't need to declare everytime

    def Old(self):
        self.year = self.year + Automobile.Time #we here implemented instance for class which will access variable from class not instance, if want to access from instance than have to declare variable in instance

Civic = Automobile(model="Civic", year="2007", type="Sedan") #we just need to add values and can be done two ways

Alto = Automobile("Alto LXI", 2019, "Hatchback" ) 

print(Alto.model, Alto.year)
Alto.Old() 
print(Alto.model, Alto.year)
print(Alto.__dict__) #to know all variables of an instance
print(Automobile.__dict__) #to know all variables of class

