# while
# 1. while loop is used for both when no of looping is fixed and also for when no of looping is not fixed
# 2. this consists (starting|stoping|upgradding) points to run a loop
# if you donot mention an upgrader then loop will run for infinite times
# Note:- while can run on both sequential and non--sequential dtype


  # initialization (starting point)
x = 1

# stopper
z = 10

# condition checker
while x <= z:
    print(x)

    # upgrader
    x += 1


guard = "hello"

while guard != "stop":
    print("ram ram")
    guard = input("Enter stop to stop:- ")

print("Loop stopped")


piggy_bank = 1000
stopper = 0

while piggy_bank > stopper:
    print("Your balance:", piggy_bank)

    withdraw = int(input("Enter the amount to withdraw: "))

    if withdraw <= piggy_bank:
        piggy_bank -= withdraw
    else:
        print("Insufficient balance")

print("Piggy bank is empty")



