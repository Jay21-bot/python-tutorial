#palindrome 

user = input("enter something: ")

rev = ""

for i in user:
  rev = i + rev

if rev ==  user: # f
  print("its palindrome")
else:
  print("its not palindrome")

# user = man
# i = m | a | n
# rev = m | am | nam

# -------------------------------------------------

# another way
# name =  "ramanujan"
# reverse = name[::-1]
# if name == reverse:
#   print("its palindrome")
# else:
#   print("its not palindrome")