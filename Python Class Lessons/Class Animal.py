from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("I can walk and run")

class Snake(Animal):

    def move(self):
        print("I can crawl")

class Dog(Animal):

    def move(self):
        print("I can bark and run")

class Werewolf(Animal):

    def move(self):
        print("I howl and run at mock speed... Good luck trying to escape....")

R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Werewolf()
K.move()
