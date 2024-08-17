class Car : 
    wheels = 4 # class varible

    def __init__(self , make , model , year , color) -> None:
        # instance varables
        self.make  = make
        self.model = model 
        self.year  = year 
        self.color = color 

    def drive(self) : 
        print("car  "+self.make+" is driving")    

    def stop(self) : 
        print(f"car {self.make} is stoped")


print(Car.wheels)

car1 = Car("chevy" , "corvette"  , "2021" , "blue")
car2 = Car("ford"  , "mustang"   , "2022"   , "reed")

print(car1.wheels)
print(car2.wheels) 

car1.drive()
car2.drive()


car1.wheels = 6 

print(car1.wheels)
print(car2.wheels) 

print("\n...................... " * 3 + "\n")
class Car : 
    
    def turn_on(self) : 
        print("car turned on ")
        return self
    
    def drive(self) : 
        print("car drive")
        return self
    
    def brak(self) : 
        print("car stoped  ")
        return self
    
    def turn_off(self) : 
        print("car turned off ")
        return self
    
class boghaty (Car):

    def drive(self) : 
        print("car drive automtic")
        return self

car =  Car()
# car.turn_on() 
# car.drive() 
# car.brak() 
# car.turn_off() 

#       method chining  : call multiple methods sequntially
# car.turn_on().drive().brak().turn_off() 
 
car.turn_on()\
    .drive()\
    .brak()\
    .turn_off()  

car = boghaty()


car.drive()      # call method in class boghaty
Car.drive(car)   # call method in class Car   

from abc import ABC , abstractmethod 
class vehicle (ABC) : 
    @abstractmethod
    def go(self) : 
        pass 
class car (vehicle) : 
    def go(self) : 
        print("go car")    

class moto (vehicle):

    def g(self) : 
        print("hello g") 

# car = vehicle()  error 

car = car() 
car.go()

# car = moto() error we shoud make implemttion go function
# car.g()