# Multiple parent class and multiple child class

class father:
  def car(self):
    print("mere pass bmw hai")

class mother:
  def home(self):
    print("mere pass ghr hai")

# inheriting father and Mother class into daughter's class
class daughter(father,mother):
  def scooter(self):
    print("mere pass ather rizta hai")

class son(father,mother):
  def bike(self):
    print("mere pass R15 hai")

d = daughter()
d.scooter()
d.car()
d.home()

print()
print("---------------------------")
print()

s = son()
s.bike()
s.car()
s.home()

print()
print("---------------------------")
print()