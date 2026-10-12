class vault:
    def locker(self,pin):
                if pin == 1234:
                    current = 1000
                    savings = 1000

                    for i in range(3):

                            pin =  int(input("enter the pin: "))
                            if pin == 1234:
                                    
                                    while True:        
                                            print("1. From saving")
                                            print("2. From Current")
                                            print("3. Cancel")
                                            
                                            choice = input("enter the choice: ")
                                            
                                            if choice == "1":
                                                    print("you've selected savings account")
                                                    print("1. withdraw")
                                                    print("2. Deposit")
                                                    print("3. Cancel")
                                                    
                                                    option = input("enter the option: ")
                                                    
                                                    if option == "1":
                                                            print("you've selected to withdraw")
                                                            amnt = int(input("enter the amnt. to withdraw: "))
                                                            if amnt < savings:
                                                                savings -= amnt
                                                                print("you've withraw amnt: ", amnt)
                                                                print("reamining balance: ",savings)                        
                                                            else:
                                                                print("insuffecient balalnce")
                                                                                            
                                                    elif option == "2":
                                                            print("you've selected for depost")
                                                            amnt = int(input("enter the amnt to deposit: "))
                                                            savings += amnt
                                                            print("you've deposited : ",amnt)
                                                            print("your balance : ",savings)

                                                    elif option == "3":
                                                        print("you've pressed an cancel button ")
                                                        break
                                                    
                                                    else:
                                                        print("something went wrong")
                                                    
                                            elif choice == "2":
                                                        print("you've selected current acount account")
                                                        print("1. withdraw")
                                                        print("2. Deposit")    
                                                        print("3. Cancel")
                                                        
                                                        option = input("enter the option: ")
                                                        
                                                        if option == "1":
                                                                print("you've selected to withdraw")
                                                                amnt = int(input("enter the amnt. to withdraw: "))
                                                                if amnt < current:
                                                                    current -= amnt
                                                                    print("you've withraw amnt: ", amnt)
                                                                    print("reamining balance: ",current)                        
                                                                else:
                                                                    print("insuffecient balalnce")

                                                        elif option == "2":
                                                                print("you've selected for depost")
                                                                amnt = int(input("enter the amnt to deposit: "))
                                                                current += amnt
                                                                print("you've deposited : ",amnt)
                                                                print("your balance : ",current)

                                                        elif option == "3":
                                                            print("you've pressed an cancel button")
                                                            break
                                                        
                                                        else:
                                                            print("something went wrong")
                                            
                                            elif choice == "3":
                                                print("you've pressed an cancel button")
                                                break
                                                        
                                            else:
                                                print("something went wrong")
                                        
                            else:
                                print("wrong pin no.")

                    print("try after 24 hours")
            
            
            
def passcode():
    return 1234