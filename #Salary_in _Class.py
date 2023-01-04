class Salary:

    def __init__(self,hours,rate):
        self.hours = hours
        self.rate = rate

    def pay (self):
        if self.hours <= 40:
            gpay = self.hours*self.rate
        elif self.hours > 40:
            gpay = ((self.hours-40)*(1.5*self.rate))+40*self.rate
        print(gpay)
        
Employee1 = Salary(39, 10)
Employee2 = Salary(45, 10)

Employee1.pay()
Employee2.pay()

