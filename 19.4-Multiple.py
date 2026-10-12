# Multiple parent class but single child class

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


d = daughter()
d.scooter()
# accessing the parents class's function with child class's object
d.car()
d.home()

print()
print("---------------------------")
print()