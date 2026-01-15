class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery,Engine,Car): 
    pass


my_newCar = ElectricCarTwo("tesla","model s")
print(my_newCar.engine_info())
print(my_newCar.battery_info())