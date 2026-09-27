from abc import ABC, abstractmethod

class Absclass(ABC):

    def print (self, x):
        print("Passed value is: ", x)

    @abstractmethod
    def task(self):
        print("This is inside abstract task")

class test_class(Absclass):

    def task(self):
        print("This is inside task method of test_class")

test_obj = test_class()
test_obj.task()
test_obj.print(100)