# kwargs :-  keyword arbitratory arguements
# kwargs used to take user input in  pairs
# to create an kwargs use ** before name of ur parameter
# kwargs used to store arguements in dictionary

# note :-  make sure to pass arguemnets in pairs only


class data:
    def register(self,**d):
        print("dtype of d :" , type(d))
        print()
        for i,j in d.items():
            print(f"{i} : {j}")
        # print(d)

print()
print("---------------------------------------")
print()

d1 = data()
d1.register(name = "damini" , age = 22 , salary = 30000 , dept = "IT")

print()
print("---------------------------------------")
print()

d2 = data()
d2.register(name = "damini" , age = 22 , salary = 30000 , dept = "IT")

print()
print("---------------------------------------")
print()

d3 = data()
d3.register()

print()
print("---------------------------------------")
print()

