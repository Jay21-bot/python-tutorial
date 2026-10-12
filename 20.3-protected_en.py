# protrected encapsulation

# any function becomes protected function when its name starts with single underscore (' _ ')
# (use single underscore as first character of your funtion's name to make it protected fucntion)

# A protected function exaclty works like a public function
# Major difference in between the 2 is :
#                                    a. public function can be called from anywhere
#                                    b. protected function can also be called from anywhere but not recommended to be called by its own class's object


class safe:
  def _protected(self):
    print("protected function")


print("calling a function in this way is possible but not recomended")
print("calling a function by its own class's object")
s = safe()
s._protected()

print()
print("--------------------------------------------")
print()

class encapulation:
  def capsule(self):
    safe._protected(self)

print("calling a function with encapsulation")
e = encapulation()
e.capsule()

print()
print("--------------------------------------------")
print()

class inheritance(safe):
  def heritage(self):
    print("heritage function")
    safe._protected(self)

print("calling a function with inheritance")
i = inheritance()
i.heritage()

print()

print("calling a function with its child class's object")
i._protected()

print()
print("--------------------------------------------")
print()