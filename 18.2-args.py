# args := arbiratory arguemnets
# args used to create a tuple typeof parameter for a function to take multiple arguement at a time
# do not create multiple parameters to take multiple arguements -
# -just create an args and this used to store miltiple arguement as a element of the args(tuple)

# to create an args use single asterisk ('*') before name of the parameter
# '*' is not the part of paraemter its just a component of args(use name of the parameter directly without '*')
# in real args used to create a tuple as a parameter

# keep 3 things in mind before creating an args 
# 1 :- use single '*' before name of the parameter
# 2 :- name a parameter by applying the rules of variable
# 3 :- do not assign a default value to ur args

# u can typecast ur args later in list if u have to perform any mutability task

class calc:

  # *num is the actual args
  def add(self,*num):
    print("type of num :" , type(num))
    print("values in num :" , num)
    print("------------------")
    # num = list(num)
    for i in num:
        print(i)
    # print("sum :", sum(num))


c =  calc()
c.add(12,4.5,"hello",True,None,[1,2,3],{1,2,2},(1,2,3))