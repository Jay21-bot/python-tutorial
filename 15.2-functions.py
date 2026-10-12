# no return no parameter
def greet():
  for i in range(5):
    print(i,'happy new year')

greet()  
  
  # ------------------------------------------------------------------------------------
  
  
  
  # no return with parameter 

def add(x,y):
  print(x + y)

add(1,1)

# --------------------------------------------------------
# another eg.

def car(key,fuel):
  if key == "remote" and fuel == "petrol":
    print("car started")
  else:
    print("anti theft alarm started")

car("chabi" , "petrol")


  
  # ------------------------------------------------------------------------------------
  
  
  # with return no parameter

def birthday():
  return "gift"

# this will only return o/p if there is nothing below it
birthday()

print(birthday()) #use this if return fucntion has something below it

# --------------------------------------
# anohter eg.

def num():
  return 10
x = num()
print(x)

# --------------------------------------
# anohter eg.

def another():
  print("hello its another level")
  return 5

# as fucntion called print statement will execute
# but the 5 returned to the z 
z = another()

# to get 5 print z
print(z)
  
  
  # ------------------------------------------------------------------------------------
  
  
  # with return with parameter

def speed(distance,time):
  return distance // time

lap1 = speed(45,5)
print("lap1 :-" , lap1)

lap2 = speed(95,5)
print("lap2 :-" , lap2)

# -----------------------------------------------------

def atom_nuber(proton,neutron):
  return proton - neutron

print(atom_nuber(2,1))
  
  
  # ------------------------------------------------------------------------------------
  
  












  
  
# ai


# ============================================================
# 1. NO RETURN, NO PARAMETER
# ============================================================

def greet():
    for i in range(5):
        print(i, "happy new year")


greet()


# ============================================================
# 2. NO RETURN, WITH PARAMETER
# ============================================================

def add(x, y):
    print(x + y)


add(1, 1)


# Another example


def car(key, fuel):
    if key == "remote" and fuel == "petrol":
        print("car started")
    else:
        print("anti theft alarm started")


car("chabi", "petrol")


# ============================================================
# 3. WITH RETURN, NO PARAMETER
# ============================================================

def birthday():
    return "gift"


# Calling the function without print()
birthday()

# Use print() to display the returned value
print(birthday())


# Another example


def num():
    return 10


x = num()
print(x)


# Another example


def another():
    print("hello its another level")
    return 5


# When the function is called, the print statement executes.
# The value 5 is returned and stored in z.

z = another()

# Print z to display the returned value.
print(z)


# ============================================================
# 4. WITH RETURN, WITH PARAMETER
# ============================================================

def speed(distance, time):
    return distance // time


lap1 = speed(45, 5)
print("lap1:", lap1)

lap2 = speed(95, 5)
print("lap2:", lap2)


# Another example


def atom_number(proton, neutron):
    return proton - neutron


print(atom_number(2, 1))