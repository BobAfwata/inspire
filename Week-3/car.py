class car:
    def __init__(self,model,make,year_of_man,engine_capacity):
        self.model = model
        self.make = make
        self.year_of_man = year_of_man
        self.engine_capacity = engine_capacity

    #getters
    def get_model(self):
        return self.model 
    
    def get_make(self):
        return self.make
    
    def get_year(self):
        return self.year_of_man
    

    #setters : set the attributes 
    def set_model(self,model):
        self.model = model

    def set_make(self,make):
        self.make = make

    def set_year(self,year_of_man):
        self.year_of_man = year_of_man

    
    
#objects : instances of the class 
car1 = car("demio","nissan",2018,1300)
car2 = car("hilux","toyota",2020,3500)
car3 = car("passat","vw",2009,2600)



car3.set_year(2023)
car1.set_year(2026)
car1.set_model("toureg")


print(car1.get_model())
print(car1.get_year())

print(car2.get_model())
print(car3.get_year())


print(car1.get_year())
print(car3.get_year())