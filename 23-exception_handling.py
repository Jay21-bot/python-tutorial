# exception handling 
# the main purpose to use exception is to reduce the error in output even after the mistake in program

# exception handling slightly works like a conditional statement

# but

# the major difference in between exception handling and conditonal statement is 

# conditional statment use to check multiple condition and executes the statement when condition is true

# on the other hand 

# exception handling used to execute the statement when the particular type of error occurs in the programme


# try,except and finally is a keyword 
# used as a component of exception handling

try:    
    # if this works than everything will remain normal
    # print(10/2)
    
    # but if u try to do this
    print(10/0)

    # than instead of giving an error it will return something that u want to print on screen after the zerodivision error
except ZeroDivisionError:
    print("cannot divide by zero")

# this always used to get executed no matter what when u apply this in exception handling
finally:
    print("exception handling appliaed")
    
    
    
    
# you need to have a brief knowledge about the category of errors to use exception handling 
# for eg :- zerodivisioneror (occurs when num is tried to divide by 0),
#        :- syntaxerror (occurs when syntax is not correct),
#        :- typerror :- (occurs when you enter the wrong dtype ),etc

# don't be worried about this, if u don't have a much idea about the errors

# just use exception as e 
# and this used to cover all your errors


print("------------------------------------")

try:
    print(10 / 0)
            
# use 'Exception as e' when u don't have an enough knowlegde about errors
# exception keyword used when u don't know about the error and it wil figure it out about the error and excutes your exception statement instead of returning an error
except Exception as e:
    print("something went wrong")
    # if u print 'e' it will return the type of an error in output as well
    print("the type of error is :-" , e)
    
print("------------------------------------")