class Computer:
    def __init__(self):
        self.max_price = 900

    def sell(self):
        print("Selling Price: {}".format(self.max_price))

    def set_max_price(self, price):
        self.max_price = price

c = Computer()
c.sell()

c.__max_price = 1000
c.sell()


c.set_max_price(1000)
c.sell()


 
