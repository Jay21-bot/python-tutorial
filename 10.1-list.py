# list dtypes in python
#    (list dtype can store almost every dtype's of data)
# 1. its used to store multiple elements of diff.-diff. dtype or may be of similiar dtype
# 2. to create a list you need to put elements in '[ ]' sqr. brckts. and seperate it with ','
# 3. U can put list under the list as well
# 4. u can access or manipulate the list's data with its own predefined functions
# 5. concepts like indexing,slicing,step is applicapable

# Nature :- List is mutable in Nature
#           (mutable means u can change the list's data with its own functions)

print()
print("----------------------------------------------------------------")
print()

# int dtype's list
# some maths functions with list

# Note :- this functions only works when lsit has int or float elements
L1 = [1,2,3,4,5,6,7,8,9,10]

print("Dtype of L1: ",type(L1))
print("Values of L1: ",L1)
print()
print("Sum: ",sum(L1)) # returns the total of elements
print("Min: ",min(L1)) # returns min value of element from the list
print("Max: ",max(L1)) # Returns max value of lsit
print("Length: ",len(L1))

print()
print("----------------------------------------------------------------")
print()

# mixed dtype's list


print("Dtype of L2: ",type(l2))
print("Values of L2: ",l2)

x = 10
L2 = [1,2,3,2,2,"hello",x,"name",True]

# to get all list function
# 1. type Variable's name and than type ' . ' only that this will show suggestions

L2.append("ram")# used to add single elements at the last

L2.extend([30,40,"bhuvan",False]) # used to add multiple elements at last in list 

L2.insert(1,"ravi") # used to add single element at particular index position in list

L2.insert(4,[4,5,6]) # used to add list at particular index position in list

# a = [1,3,5,7,4,2,10]
# print("before sorting: ",a)
# a.sort() # used to sort numeric list in ascending
# print("after sorting:",a)

# print("Before: ",L2)
# L2.pop() # used to pop the last element of the lsit
# print("After: ",L2)

# L2.remove("ravi") # used to remove a particular element form the list

# L2.clear() # used to delete elements of the list and rest its structure

# L2.reverse() #used to reverse the list

# L2.count(2) # used to particular no. of elements from the lsit

# print(L2[1]) # u can access elements by indexing as well

# print(L2[4:8]) # u can access elements by indexing + slicing as well

# print(L2[::2]) # u can access elements by indexing+slicing+step as well


print()
print("----------------------------------------------------------------")
print()
