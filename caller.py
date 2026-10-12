
# 1. from
# 2. (file name)
# 3. import
# 4. (classname) abstraction clas
# 5. (function name) abstraction method

from module  import student, id_cardno

# note:- 
# 1. no matter what always make sure to call a function in a varibale
# bcoz if the function has return type than it will return the value of a function in that particular variable and calls the function as well
# after that if u print the variable you'll get your return value in output

# calling a function in x variable
x = id_cardno()

# creating an object for student abstarct class
s = student()

# calling abstracted method of abstraction class by its object
s.stud_id(x)



# the major purpose of this programm is 
# only that person who has a knowlege of class or method can only use this code 
# because only the programmer and the person know how this code works
    