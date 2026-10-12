level = 1
while True:
    print('you are at :', level)
    
    op=input('enter next to continue to next level: ')
    
    if op =='next' or op == 'Next':
        level+=1
    
    elif op == "stop" or op == 'Stop':
        print("we'll see you soon")
        break
    
    else:
        print("something went wrong")
        
        
    
    
            
        
        
    