
# 1. recursion is a concept in a function
# 2. function calling itself is recursion
# 3. reacts like mirror effect
# 4. it is alternative of loop and stops with return keyword only

# Note :- make sure ur recursion function should be of with return with parameter

# there are two types of recusrion exist in python: (a)-direct recursion
#                                                   (b)-indirect recursion 

print()
print("------------------------------------------------------------------")
print()

print("direct recursion\n")

def recursion(x):
  if x == 0: # f | f | f | f | f | t
   #this return will stop the recusrion function when if condtion is true 
    return
  print("recusrion: " , x)
  # this works as a uograder to update the value of x
  x -= 1

  # function calling itself
  # this is essence that makes any function work recursively
  recursion(x)


# its starter of the recursion
recursion(5)


# x = 5 | 4 | 3 | 2 | 1 | 0
# op = r5 | r4 | r3 | r2 | r1

print()
print("------------------------------------------------------------------")
print()

print("indirect recursion\n")

def first(x):
  if x == 0:
    return
  print(x , ": first")
  x -= 1
  second(x)

def second(x):
  if x == 0:
    return 
  print(x , ": second")
  x -= 1
  first(x)

first(26)

print()
print("------------------------------------------------------------------")
print()