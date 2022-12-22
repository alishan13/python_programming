# multiple copies 
# 2 type : overloading and overriding
# OVERLOADING
 # operator overloading (operators have different functionality based on usage 10+20=30,Ann+Ben=AnnBen 
 # method overloading (functions with many functionalities and arguments)
# OVERRIDING
 # method overriding (used in inheritence)
'''
#Method overloading
class moveload:
    def display(self,a=None,b="Done"):
        print(a,b)
obj=moveload()
obj.display()
obj.display(10)
obj.display(10,20)
'''
#method overriding
class father:
    def transportation(self):
        print("Cycle")
class son(father):
    def transportation(self):
        print("Bike")
obj=son()
obj.transportation()