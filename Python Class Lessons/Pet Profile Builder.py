class Pet:
    def __init__(self, name, age, animal_type, color, owner):
        self.name = name
        self.age = age
        self.animal_type = animal_type
        self.color = color
        self.owner = owner

    def profile(self):
        return (
            f"Pet Profile:\n"
            f"Name: {self.name}\n"
            f"Animal Type: {self.animal_type}\n"
            f"Age: {self.age} years\n"
            f"Color: {self.color}\n"
            f"Owner: {self.owner}"
        )


pet1 = Pet("Buddy", 3, "Dog", "Brown", "Aiden")
pet2 = Pet("Milo", 2, "Cat", "Black", "Sana")

print(pet1.profile())
print()
print(pet2.profile())
