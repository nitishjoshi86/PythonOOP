#Wednesday

class Automobile:
    
    Time = 3
    
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

#above is the template kind of class, where we don't need to declare everytime

    def Old(self):
        self.year = int(self.year + Automobile.Time) #we here implemented instance for class which will access variable from class not instance, if want to access from instance than have to declare variable in instance

    @classmethod
    def Change_old(cls, addition):
        cls.Time = addition #here we will call class variable

    @classmethod
    def from_str(cls, car_string):
        model, year, price = car_string.split(",")  #it will split the values with ,
        return cls(model, year, price)
    
    @staticmethod
    def isshowroomopen(day):
        if day == 'Sunday':   #it will return boolean value
            return False
        else:
            return True

    def __add__(self,other):
        return self.price + other.price  #it will add value

    def __repr__(self):
        return 'Automobile ({}, {}, {})'.format(self.model, self.year, self.price) #formats string 

    def __str__(self) -> str:
        return 'The name of the model is {}'.format(self.model)  #this is also dunder method

""" Honda = Automobile(model="Civic", year="2007", price=600000) #we just need to add values and can be done two ways

Alto = Automobile("Alto LXI", 2019, "Hatchback" ) 

Hyundai = Automobile.from_str("Hyundai-i20, 2018, 800000") 
 """
Alto = Automobile('LXI', 2021, 356000)
Altos = Automobile('ZXI', 2021, 556000)


print(Alto + Altos)
print(Alto)
"""print(Hyundai.model, Hyundai.price) """


""" class Prevalue(Automobile):
    
    def __init__(self, model, year, price, Lprice, depreciation):
        super().__init__(model, year, price)
        self.Lprice = Lprice
        self.depreciation = depreciation """

""" WagonR = Automobile("WagonR", 2020, 356000)
WagonRS = Automobile("WagonR", 2021, 556000) """