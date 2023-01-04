#Class exercise in Python
class Cars :
   def __init__ (self,body_type,fuel,gearbox,acceleration,cylenders):
      self.body_type = body_type
      self.fuel = fuel
      self.gearbox = gearbox
      self.acceleration = acceleration
      self.cylenders = cylenders
obj_car1 = Cars ('sedan','petrol','auto',7,4)
obj_car2 = Cars('SUV','diesel','auto',8,6)
#print(obj_car1.fuel)
#print(obj_car2.acceleration)
def car_class(self):
    if self.acceleration <=7:
            print ('Race car')
    else:
            print('City car')
car_class(obj_car1)
car_class(obj_car2)
