# objects

# objects is used to store the class and its interanl data as well

class greeting:

  # to create an object of a class u need to create a self parameter in function
  # self parameter does not required an arguement to be passed 
  def birthday(self):
    print("happy birthday")

  def anniversary(self):
    print("happy anniversary")


# note :- if you  use self parameter in methods its required to create an object
# without creating an object while using self parameter its impossible to call class's function

# this will not work as it does not have any object to call the function
# greeting.anniversary()


# in general object is a variable
# an varibale is called as a object when it used to store the class and its data
# objects are used as a reference of a class to call its functions

# g is object
g = greeting()
g.birthday()
g.anniversary()


# --------------------------------------------------------------------------------------------------------------------------------------

# use case of class and objects

class std_data:
  def register(self,name,rollno,branch):
    print("Name :" , name)
    print("Roll No :" , rollno)
    print("Branch :" , branch)

# u can create multiple objects of a same class to store different category of data


print()
print("--------------------------------------")
print()

# s1,s2,s3,s4 obejct is used to store data of diff. students from a single class
# using same class but different object its possible to store multiple category of data
# each object has a similar class and function but with different student of data

s1 = std_data()
s1.register("rahul",1901,"cs")

print()
print("---------------------------------------")
print()

s2 = std_data()
s2.register("ranjana",1902,"IOT")

print()
print("---------------------------------------")
print()

s3 = std_data()
s3.register("neha",1903,"IT")

print()
print("---------------------------------------")
print()

s4 = std_data()
s4.register("mahesh",1904,"AI")

print()
print("---------------------------------------")
print()

