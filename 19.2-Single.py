# Single Inheritance

# single parent class single child class

class father:
  def car(self):
    print("mere pass bmw hai")

# inheriting father class into daughter's class
class daughter(father):
  def scooter(self):
    print("mere pass ather rizta hai")

d = daughter()
d.scooter()
# accessing the parents class's function with child class's object
d.car()

print()
print("---------------------------")
print()

# Note:- parent class can not access the child class's method or data even after getting inherited

f = father()
f.car()

# this will not work
# f.scooter()