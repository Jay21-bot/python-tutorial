# constructor is called when obejct is created for class

class somthing:

  def __init__(self):
    print("constructor is called automatically")
    print("when object is created")

  def __del__(self):
    print("destructor is called automatically")
    print("when object is deleted")

# creating an object for something named class
s = somthing()

print("-----------------------------")

# delting the object of a something named class
del s
