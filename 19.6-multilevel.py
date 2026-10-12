# parent class is a child class of another parent class

class grandfather:
  def Property(self):
    print("mere pass bhot saari zameenein hai")

# father is child class of grandfather class
# father is parent class of son class
class father(grandfather):
  def car(self):
    print("mere pass BMW hai")

class son(father):
  def bike(self):
    print("mere pass pulsar hai")


# in this type ofinheritance u can not just acces the parent class funtions or data 
# but can also access the parent class's - parent class function with its object

s = son()
# accesing the own class function with its own object
s.bike()

# accessing father class's function with its own class's object
s.car()

# accessing grandfather class's function with its own class's object
# even after not inheriting it directly but indirectly with father class
s.Property()