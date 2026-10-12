class mutli_function:

  def __init__(self,x):
    # x can not be used for its sibling class function directly
    # that's we are creating 'self.z'
    # which works like a global varible of this particular class
    # and can be used in its sibling functions as well 
    self.z = x
    print("you've eneter this :" , self.z)
    print("dtype of what you've entered :" , type(self.z))

  def palindrome(self):
    if self.z.isalnum():
      rev = self.z[::-1]

      if self.z == rev:
        print(self.z , "is a palindrome")
      else:
        print(self.z , "is not a palindrome")
    
    else:
      print("its not alphanumeric string")


  def even_odd(self):
    if self.z.isdigit():
      if int(self.z) % 2 == 0:
        print(self.z , "is even")
      else:
        print(self.z , "is odd")
    else:
      print("its not a digit")

  
  def length(self):
    print("length of what you've entered :" , len(self.z))



m = mutli_function("1001")
print("------------------------")
m.even_odd()
print("------------------------")
m.palindrome()
print("------------------------")
m.length()
print("------------------------")