# duck typing

# duck typing is the process to call overidden functions of a class with new independent function
# duck typing can only be applicable for method overriding concepts

class truck:
  # overriden function/ method
  def engine(self):
    print("truck started")

class car:
  # overidden function/ method
  def engine(self):
    print("car started")

t = truck()
c = car()


# this is the actual duck type concept 
# which is used to call the overridden functions with new function
# a function calling overridden function is duck typing
# a duck type concept always uses the with parameter type of function
# about return it depends upon the requirement
def calling(x):
  x.engine()

calling(t)
calling(c) 