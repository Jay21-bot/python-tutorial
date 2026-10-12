# overlaoding
# its the proces to set default value for parameter of a function
# its not compulsory to pass an arguemnet while calling function even after the function is with parameter type
# this will not return any error if arguement is not passed as this has a default value
# the dafult value will be replaced if arguement is passed while calling the function


# Note :- python's overloading does not work like java's or c++'s overloading
#      :- because we can set default values for parameters as java and other languages do not support

# overloading type of program does not return any error if u do not pass any arguement

class maths:
  # setting a default value of a parameter is actual overloading
  def add(self,a = 0 , b = 0):
    print("sum :" , a + b)


m  = maths()


print()
print("------------------------------------------------")
print()

print("calling a fuction without passing an arguement")
print("m.add()")
m.add()

print()
print("------------------------------------------------")
print()

print("calling a function with passing only an single arguement")
print("m.add(2)")
m.add(2)

print()
print("------------------------------------------------")
print()

print("calling a function with passing an arguements")
print("m.add(2,3)")
m.add(2,3)

print()
print("------------------------------------------------")
print()