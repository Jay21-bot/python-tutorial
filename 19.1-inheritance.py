# inheritance
# its the process to access the data from parent class with its child class's object

# this is the parent class as this is inherited in betaji class
class pitaji:
  def Property(self):
    print("mere pass property hai")

# this class is child class as it inherits the pitaji class
class betaji(pitaji):
  def vehicle(self):
    print("mere pass bmw hai")


b = betaji()
b.vehicle()

# accessing the parent class's function with child class's object
# this would be only possible when betaji class inherits the pitaji class
b.Property()