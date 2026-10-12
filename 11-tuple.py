# tuple dtypes

# tuple is capable to store almost evry dtype ofelement in it
# tuple is immutable in nature
# you can only access the elements of tuple but can not maipulate the data with functions
# reinitialization or tuple concatenation is allowed
# tuple has its own predefined functions but only 2

print()
print("-----------------------------------------")
print()

print("2 Predefinded functions in tuple\n")

t = (1,2,3,3,"hello",5.6,True,2,2,23)

print("t.count(2) :" , t.count(2)) # returns how many times an particular element stated in tuple
print("t.index(\"hello\") :" , t.index("hello")) # returns the index no. of particular element


print()
print("-----------------------------------------")
print()

print("Process of reinitialisation\n")

T = (1,2,3,4,5)
print("before :" , T)

print()

T = (1,2,3,4,5,6)
print("after reinitialisation :" , T)

print()
print("-----------------------------------------")
print()

print("process of reinitialisation\n")

T = (1,2,3,4,5)
print("before :" , T)

print()

T = (1,2,3,4,5,6)
print("after reinitialisation :" , T)

print()
print("-----------------------------------------")
print()
