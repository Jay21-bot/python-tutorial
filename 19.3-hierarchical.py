# single parent class but multiple child class

class father:
  def car(self):
    print("mere pass bmw hai")

# inheriting father class into daughter's class
class daughter(father):
  def scooter(self):
    print("mere pass ather rizta hai")

class son(father):
  def bike(self):
    print("mere pass R15 hai")

d = daughter()
d.scooter()
# accessing the parents class's function with child class's object
d.car()

print()
print("---------------------------")
print()

s = son()
s.bike()
s.car()