# Simple ATM sysytem pin base
# Features: Balance check, Withdraw, Deposit, Exit

# Initial account balance
balance=5000

# Correct pin for authentication
correct_pin=1234

print("welcome to ATM")

# pin verification (Take input from user)
try:
    pin=int(input("enter your pin : "))
except:
    print("invalid pin")
    exit()
    
# Check if pin is correct 
if pin==correct_pin:
    print("login Successful")
    
# ATM menu open
    while True:
        print("\n>>> ATM MENU <<<")
        print("1. check balance")
        print("2.  Withdraw Money")
        print("3. Deposit money")
        print("4. exit")
    
        # choice number between 1 to 4
        choice=input("\nenter your choice : ")
    
        # chek bank balance
        if choice=="1":
            print("your balance is : ",balance)
    
        # Withdraw money
        elif choice=="2":
            try:
                withdraw_money=int(input("enter withdraw money : "))
            except:
                print("please enter valid money")
                continue
            if withdraw_money>0:
                if withdraw_money<=balance:
                    balance-=withdraw_money
                    print(withdraw_money," Withdraw Successful")
                    print("current balance : ",balance)
                else:
                    print("Insufficient balance")
            else:
                print("please enter valid money")
            
        # Deposit money
        elif choice=="3":
            try:
                deposit_money=int(input("enter your deposit money : "))
            except:
                print("please enter valid ammount")
                continue
            if deposit_money>0:
                balance+=deposit_money
                print("your deposit money : ",deposit_money)
                print("your current balance : ",balance)
            else:
                print("enter valid money")
        
        # Exit 
        elif choice=="4":
            print("thank you to use ATM")
            break
        # invalid choice
        else:
            print("please enter valid choice")
else:
    print("incorrect pin")
