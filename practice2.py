marks = int(input("enter the marks to check the grade: "))

if marks >= 80 and marks <= 100:
    print("grade : 'A'")
    print("your percentage is :",marks,"%")
    print('well done')
    
elif marks >= 60 and marks <= 79:
    print("grade : 'B' ")
    print("your percentage is :",marks,"%")
    print('very good ')

elif marks >= 40 and marks <= 59:
    print("grade : 'C' ")
    print("your percentage is :",marks,"%")
    print('good')

elif marks >= 33 and marks <= 39:
    print("grade : 'D' ")
    print("your percentage is :",marks,"%")
    print('need improvement')
    
elif marks >= 0 and marks <= 32:
    print('fail')
    print('compartment')

else:
    print('invalid input enter marks properly')

 
 
table = int(input('enter the number which one table you want:'))
for i in range(1,11):
    print(f"{table} x {i} = {table * i}")
 
 
      
      