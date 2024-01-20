# class Car: 
#     def __init__(self, model, year): 
#         self.model = model 
#         self.year = year 
         
         
#     def info(self): 
#         print(f"Модель - {self.model}, Год выпуска - {self.year}") 
         
# class ElectricCar(Car): 
#     def __init__(self, model, year, battery): 
#         Car.__init__(self,model, year) 
#         self.battery = battery 
         
         
#     def drive(self): 
#         print(f"Мишина - {self.model} едет на электричестве") 
         
         
# class FuelCar(Car): 
#     def __init__(self, model, year, fuel_bank): 
#         Car.__init__(self,model, year) 
#         self.fuel_bank = fuel_bank 
         
         
#     def drive(self): 
#         print(f"Мишина - {self.model} едет на топливе") 
         
         
         
# class HybridCar(ElectricCar,FuelCar): 
#     def __init__(self, model, year, battery, fuel_bank, speed): 
#         super().__init__(model, year, battery) 
#         FuelCar.__init__(self,model, year, fuel_bank) 
#         self.speed = speed 
         
         
#     def drive(self): 
#         if self.speed > 60: 
#             print(f"Машина - {self.model} едет на топливе") 
#         else: 
#             print(f"Машина - {self.model} едет на гибриде") 
                 
 
 
# tesla = ElectricCar("Tesla - Model X", 2024, 90) 
# tesla.info() 
# tesla.drive() 
 
 
# matiz = FuelCar("Matiz - 3 ", 2020, 30) 
# matiz.info() 
# matiz.drive() 
 
 
# lexus = HybridCar("Lexus - es300 ", 2020, 40, 60, 50) 
# lexus.info() 
# lexus.drive()



class Car: 
    def __init__(self, model, year): 
        self.model = model 
        self.year = year 
         
         
    def info(self): 
        print(f"Модель - {self.model}, Год выпуска - {self.year}") 


    def __str__(self):
        print(f"бренд- {self.model}, год выпуска - {self.year} ")

    def __str__(self):
        return f"бренд- {self.model}, год выпуска - {self.year} "

bmw= Car("bmw - m5", 2022)
bmw.info()