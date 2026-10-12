# constructor

# in real constructor is a function which is called automatically when class's object is created
# make sure the name of your contructor look a like this (' def __init__(self): ')
# you can assign any task to your constructor
# you can even take an arguements with parameters in this function

class result:

  # this is the real constructor
  # this constructor function will be called automatically when object is created for the class
  # this used to take an arguement when object is created for x named parameter
  def __init__(self,x):
    # create a new variable with 'self.name' to copy the value of 'x'
    # we are using 'self.name' bcoz we need to use this in sibling function.
    # 'self.name' is like a global variable for this particular class
    self.name = x
    # you can customise the task of an constructor as per your requiremnet
    print("your name is damini :" , self.name)

  def english(self):
    # using 'self.name' in the statement of sibling function
    print(f" {self.name} your marks in english is : 56")

  def Hindi(self):
    print(f" {self.name} your marks in hindi is : 56")
  
  def science(self):
    print(f" {self.name} your marks in science is : 56")
  
  def maths(self):
    print(f" {self.name} your marks in maths is : 56")

# creating an object for resul class
# we can only pass the arguement for the constructor's parameter here only before calling any funtion
# 'damini' is the arguement passed for x parameter of constructor function
r = result("damini")

# calling the function with result class's object
r.english()
r.Hindi()
r.science()
r.maths()