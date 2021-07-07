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
        model, year, price = car_string.split(",")
        return cls(model, year, price)
    
    @staticmethod
    def isshowroomopen(day):
        if day == 'Sunday':
            return False
        else:
            return True

""" Honda = Automobile(model="Civic", year="2007", price=600000) #we just need to add values and can be done two ways

Alto = Automobile("Alto LXI", 2019, "Hatchback" ) 
 """
""" Hyundai = Automobile.from_str("Hyundai-i20, 2018, 800000")

print(Hyundai.model, Hyundai.price) """


print(Automobile.isshowroomopen('Sunday'))