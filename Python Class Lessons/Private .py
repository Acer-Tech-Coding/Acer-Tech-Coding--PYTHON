class MyClass:

    __private_var = 17

    def __privMeth(self):
        print("I am inside class MyClass")

    def hello(self):
        print("Private variable is: ", MyClass.__private_var)

foo = MyClass()
foo.hello()
foo.__privMeth()  