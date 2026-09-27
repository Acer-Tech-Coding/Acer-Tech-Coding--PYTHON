class Renault_Vehicle:
    def __init__(self, type, horsepower, model, safety_rating, seats): 
        self.type = type
        self.horsepower = horsepower
        self.model = model
        self.safety_rating = safety_rating
        self.seats = seats

    def show_traits(self):
        print("Type: ", self.type)
        print("Horsepower: ", self.horsepower)
        print("Model: ", self.model)
        print("Safety Rating: ", self.safety_rating)
        print("Seats: ", self.seats)


class Model(Renault_Vehicle):

    def __init__(self, type, horsepower, model, safety_rating, seats):
        
        super().__init__(type, horsepower, model, safety_rating, seats)

    def show_traits(self):
        print("Model: ", self.model)
        print("Type: ", self.type)
        print("Horsepower: ", self.horsepower)
        print("Safety Rating: ", self.safety_rating)
        print("Seats: ", self.seats)
        

model1 = Model("Compact SUV", 100, "Kiger", 4, 5)
model1.show_traits()
print("\n")

model2 = Model("Hatchback", 70, "Kwid", 2, 5)
model2.show_traits()
print("\n")

model3 = Model("MPV", 70, "Triber", 4, "5 or 7")
model3.show_traits()
print("\n")

model4 = Model("SUV/MPV", 170, "DUSTER", 5, "5 or 7")
model4.show_traits()
