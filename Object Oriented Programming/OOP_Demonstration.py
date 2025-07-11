class Car:
    def __init__(self, model, manufacturer_year, color, for_sale):
        self.model=model
        self.manufacturer_year=manufacturer_year
        self.color=color
        self.for_sale=for_sale
    
    def drive(self):
        print(f"You drive the {self.color} {self.model} car")
    
    def stop(self):
        print(f"You stopped the {self.color} {self.model} car")
    
    def describe(self):
        print(f"{self.manufacturer_year} {self.color} {self.model}")


bmw_car= Car("BMW",2025,"Black",False)
# print(bmw_car.model)
# print(bmw_car.manufacturer_year)
# print(bmw_car.color)
# print(bmw_car.for_sale)
bmw_car.drive()
bmw_car.stop()
bmw_car.describe()

corolla_car= Car("Corolla",2024,"White",True)
# print(corolla_car.model)
# print(corolla_car.manufacturer_year)
# print(corolla_car.color)
# print(corolla_car.for_sale)
corolla_car.drive()
corolla_car.stop()
corolla_car.describe()

cultus_car= Car("Cultus",2023,"Blue",False)
# print(cultus_car.model)
# print(cultus_car.manufacturer_year)
# print(cultus_car.color)
# print(cultus_car.for_sale)
cultus_car.drive()
cultus_car.stop()
cultus_car.drive()
