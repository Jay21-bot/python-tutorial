# predefined abstraction

# abc :- is an actual predefined module of python which comes at the time of installation of python's interpreter

# ABC :- is the actual abstract class

# abstractmethod :- is the actual abctractmethod

from abc import ABC , abstractmethod

# note :- if the 'father' class wants its child class to create an learning function than parent class needs to use abstract class to inherit and use abstract method


# parent class inheriting the 'ABC' class which was import at the beginning from 'abc' module
class father(ABC):
    def car(self):
        print("mere pass BMW hai")

    # suppose if i want this function to be created in child class
    # so i need to make it abstract method
    # to create this an abstarctnethd " i'll do this "
    @abstractmethod
    def learning(self):
        print("i believe in contineous learning")

# son class inheriting the father class
class son(father):
    def bike(self):
        print("mere pass pulsor hai")

# daughter class inheriting the father class
class daughter(father):
    def scooter(self):
        print("mere pass active hai")
        
    def learning(self):
        print("i believe in essential learning ")
        
print()
print("-------------------------")
print()

# as son inherits the father class 
# and father class created a rule that every child class needs to create an lerning function in it 
# so son can not call its own function utill it create a function with the name of learning as it inherits the father class
# s = son()
# s.bike()
# s.car()

print()
print("-------------------------")
print()
        
d = daughter()
d.scooter()
d.car()

print()
print("-------------------------")
print()