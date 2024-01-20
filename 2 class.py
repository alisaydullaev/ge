class Animal:
    def __init__(self,breed,classes,year, color):
        self.breed=breed
        self.year=year
        self.color=color
        self.clases=classes 

        def info (self):
            print(f"{self.breed},{self.classes},{self.year},{self.color}")


class Dog (Animal) :
    pass
# dog = Animal (" haski", "млекопитающий", "grey", 3)
# dog.info()
        
def __init__(self,breed,classes,year, color):
  super.__init__(breed,classes,year, color)