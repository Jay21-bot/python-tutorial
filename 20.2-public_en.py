class sarkari:
  def public(self):
    print("its public function")

print("1. calling function by its own class's object")
s = sarkari()
s.public()

print()
print("--------------------------------------------")
print()

class inheritance(sarkari):
  def heritage(self):
    print("its heritage function")

print("2. calling by its child class's object")
i = inheritance()
i.public()
i.heritage()

print()
print("--------------------------------------------")
print()

class encapulation:
  def calling(self):
    sarkari.public(self)

print("3. calling function with encapulation withhout inheritance")
e = encapulation()
e.calling()

print()
print("--------------------------------------------")
print()

class Hybrid(sarkari):
  def bulawa(self):
    self.public()

print("4. calling function with encapulation with inheritance")
h = Hybrid()
h.bulawa()

print()
print("--------------------------------------------")
print()