# def decorator(x):

#   def wrapper():
#     print("before")
#     x()
#     print("after")

#   wrapper()


# @decorator
# def fun():
#   print("function passed as an arguement to call decorator")




# -----------------------------------------------------------




# decorator 
# its all about calling the function by passing another function as arguements


# this is the outer fucntion which takes arguements in 'event' parameter
def deocrator(event):
  
  # this is the inner function
  # inner function is also called a wrapper in python
  def theme():
    # task aasigned to theme function
    print("theme for :- " , end = "")
    # here is the main work of decorator will be performed as its task
    # event is parameter but as it holds another function as an arguement
    # that's why it has a power to call that particular function
    # make sure to apply '()' after the name of the parameter to call the function
    event()


  # the internal function needs to be called only inside the decorator function
  theme()


# do not use the ordinary technique to call decorator function

# use '@' just before the name of the 'decorator' function to cal it 
@deocrator

# do not use '()' to pass an arguements
# to pass an arguement u need to create another function here only
# and that particular function will be passed as an arguemet in the event parameter
def ocassion():
  print("the anniverary")