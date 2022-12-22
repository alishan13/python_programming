# Data Encapsulation
# wrap (combine) data and functions

class encap:
    __a=10
    def __display(self):
        print("values is :",self.__a)
    def show(self):
        print("Calling display...")
        self.__display()
obj=encap()
obj.show()
