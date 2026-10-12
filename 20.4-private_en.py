# private encapsulation

# private function can only be called by its sibling function
# put double underscore before your function's name to make it private function

class secure:
  def __private(self):
    print("its private function")

  def sibling(self):
    print("sibling function")
    self.__private()

# calling a function by its own class's object is not possible
# s = secure()
# s.__private()

print("calling a private function by its sibling function")
s = secure()
s.sibling()

print()
print("------------------------------------------------")
print()

class encapulation:
  def calling(self):
    secure.__private(self)

# even calling in this way is not possible as well

# e = encapulation()
# e.calling()

print()
print("------------------------------------------------")
print()

class inheritance(secure):
  def heritage(self):
    print("inherited function")

print("calling a sibling function with its child class's object")
i = inheritance()
i.sibling()