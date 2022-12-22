#Abstration
# concrete class and abstract class
# hiding the implimentation details
# abstract method : only declaration

from abc import ABC,abstractmethod
class Aclass(ABC):
    @abstractmethod
    def display(self):
        None
    @abstractmethod
    def show(self):
        None
class Demo(Aclass):
    def display(self):
        print("abstract method")
    def show(self):
        print("abstract show method")
obj=Demo()
obj.display()
obj.show()
        
