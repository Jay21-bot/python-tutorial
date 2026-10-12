# polymorphism

# method overriding
# functions or methods with same name but belongs to different classes are overiding
# u can assign a task to ur function as per ur requirement
# (it can be similar or may be diff. as well)

# requirement of method overriding
# u can not create a fucntion with name more then 1 time 
# otherwise it will update the task of a fucntion but can not create the new one
# which is possible by method overriding only using class and object

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

t.engine()
c.engine()
