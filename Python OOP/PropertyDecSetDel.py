class Automobile:
    
    Time = 3
    
    def __init__(self, model, year, price, color):
        self.model = model
        self.year = year
        self.price = price
        self.color = color
        self.service = model + color + 'service cost 3600' 

#above is the template kind of class, where we don't need to declare everytime

    def Old(self):
        self.year = int(self.year + Automobile.Time) #we here implemented instance for class which will access variable from class not instance, if want to access from instance than have to declare variable in instance

    @classmethod
    def Change_old(cls, addition):
        cls.Time = addition #here we will call class variable

    @property
    def service(self):
        return self.model + '.' + self.color + 'Service value is changed' #property decorator
    
    @service.setter
    def service(self, service_price):
        service_price.split(' ')[0].split    

    @classmethod
    def from_str(cls, car_string):
        model, year, price, color = car_string.split(",")  #it will split the values with ,
        return cls(model, year, price, color)
    
    @staticmethod
    def isshowroomopen(day):
        if day == 'Sunday':   #it will return boolean value
            return False
        else:
            return True




if __name__ == '__main__':
    Alto = Automobile('LXI', 2021, 356000, 'Red')
    Altos = Automobile('ZXI', 2021, 556000, 'White')
    Alto.color = 'Yellow'
    
    