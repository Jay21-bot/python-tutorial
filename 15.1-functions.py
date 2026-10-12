# defined functions 
# this are the function that programmer creates as per the requirement
# anything which reduces the code and makes it reusable than its a function

# for eg:


# you need to def keyword to create a function
# make sure to name a function by keeping the variable rules in mind
def greet():
  # you can assign almost any kind of task to be performed
  print("hello guys")

# creating a function is not enough
# we need to call the functionto use it 
greet()




# -------------------------------------------------------------------------------------------------------------------

# What is Return ?


# return is a keyword
# its used to end the fucntion by returning something
# task below return will not be executed

def bdday():

  # this will be executed when function is called no matter what
  # as it's written above the return so its the part of a function 
  print("best wishes for ur birthday")

  # 'gifts' will only be returned if the function called lastly and no other task is performed after calling the function 
  return "gifts"

  # this will not be executed as it written below return
  print("happy birthday")


# as i've used a print fucntion after calling bdday 
# so it will not return the value of return keyword in o/p
bdday()

print()
print("--------------------------------------")
print()

# this will help to get the return value if a task is performed after calling the funtion
x = bdday()
print(x)

print("hello")

print()
print("--------------------------------------")
print()

# this will print the return's value as well because no such task is performed after callinmg the function
bdday()


# -------------------------------------------------------------------------------------------------------------------




# What is Parameters

# in real parameters are variables to store a value

# x and y are the parameters for the fuinction to run
# Note:- when a function uses parameter than it should be filled with the data

def add(x,y):
  # assigning a task
  print("sum :" , x + y)


# arguements :- passing a value for a function's parameter is arguements
# Note:- 5,4 is the value to fill the data in x and y
# warning :- paasing a value is compulsory when function has a parameter othewise it will return the error

add(5,4)

# -------------------------------------------------------------------------------------------------------------------
