# set dtype
# generaly returns output in unorederd structure
# removes duplicacy from the data
# indexing slicing can not be applied
# set is unable to store list init
# set is mutable in nature

s = {True,1,3,3,"hello","man",2,24,2,13,1,"hello",True,False,(1,31,2)}

s.add("ram") #used to add elements in set

s.pop() #used to remove elements from the data

s.remove("man") #used to remove particular elements from the data

s.discard("world") #used to remove particular elements from the data and if data doesn't exist it won't return the error

s1 = {1,21,"major"}

s2 = {"@" , 4.5 ,True}

s1.union(s2)

s1.intersection(s2)

s1.difference(s2)

s.clear() # used to remove all the elements from data but let its structure void
