# # function 

# class Animal:
#     def __init__(self,leg,ear,tail):
#         self.leg = leg
#         self.ear = ear 
#         self.tail = tail

#     def display(self):
#         print(self.leg)
#         print(self.ear)
#         print(self.tail)

# Dog = Animal(4,2,1)
# Dog.display()

# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

# class Car(Vehicle):
#     def __init__(self, make, model, year):
#         # Call the constructor of the base class (Vehicle)
#         super().__init__(make, model)
#         self.year = year

# # Example usage
# vehicle_instance = Vehicle(make="Toyota", model="Camry")
# car_instance = Car(make="Honda", model="Accord", year=2022)

# # Accessing attributes from both base and derived classes
# print(f"Vehicle: {vehicle_instance.make} {vehicle_instance.model}")
# print(f"Car:
#  {car_instance.make} {car_instance.model} ({car_instance.year})")



class vehicle:
    def __init__ (self,make,model):
        self.make=make
        self.model=model

class cycle:
    def __init__(self,wheel):
        self.wheel = wheel

class car(vehicle,cycle):
    def __init__ (self,make,model,year,wheel):
        self.year=year
        # print(f" year was {year},{model} was made by {make}")
        # super().__init__(make,model)
        super().__init__(wheel)

# a=car("buggatti","buggati veyron",1992)
b = car("Ferrari","wolkskwagon", 2025,4)

print(b.wheel)





# datetime library 
# strftime()



