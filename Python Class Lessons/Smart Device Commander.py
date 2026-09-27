from abc import ABC, abstractmethod

class Device(ABC):

    @abstractmethod
    def activate(self):
        pass

class PC(Device):

    def activate(self):
        print("I am a bit large but am perfect for gaming and work. I am used worldwide and am very powerful..")

class Laptop(Device):

    def activate(self):
        print("I can be carried around and are great for portability. I am also used for gaming and work but not as powerful as a PC.")

class Smartphone(Device):

    def activate(self):
        print("I can make calls and access the internet. I am very convenient for communication. And i am the most used device in the world. I am also used for gaming and work but not as powerful as a PC or Laptop.")

class Tablet(Device):

    def activate(self):
        print("I am a portable device that combines the features of a laptop and a smartphone. I am used for media consumption and light productivity tasks. I am mainly used by buisiness professionals and students. But I am not as powerful as a PC or Laptop.")

R = PC()
R.activate()
print("\n")

K = Laptop()
K.activate()
print("\n")

R = Smartphone()
R.activate()
print("\n")

K = Tablet()
K.activate()
print("\n")
