# classes

# classes are used to store set of functions and its data togther

# maths class used to store multiple functions and its data together
class maths:

  # functions in class also called as methods
  def add(x,y):
    print("sum :" , x + y)

  def sub(x,y):
    print("difference :" , x - y)

  def mul(x,y):
    print("product :" , x * y)

  def div(x,y):
    print("quotient :" , x / y)

# u need to call a function by its class's name
maths.add(10,20)
maths.sub(10,20)
maths.mul(10,20)
maths.div(10,20)

# features:-
# different class can store function with same name
# functions of a class cannot be called without its class's name
# class not just hold the function but also its data as well
# without class concepts of oop's cannot be applicable
# classes used to categorise the funtion in parts
# Nested class is allowed to be created with some limitations

class parent:
  class child:
    def add(x,y):
      print("sum :" , x + y)

    def sub(x,y):
      print("difference :" , x - y)
