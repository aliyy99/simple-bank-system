import datetime
def get_time():
    return datetime.datetime.now().strftime("%X")
def create_account(owner_name):
    return {"owner":owner_name,"balance":0}
def deposit(account,amount):
    if amount>0:
        account["balance"]+=amount    
        print(f"{amount} TL deposited successfully. Current balance:{account["balance"]} TL")
    else:
        print("the amount to be deposited must be positive")
def withdraw(account,amount):
    if amount>0:
        if account["balance"]>=amount:
           account["balance"]-=amount
           print(f"{amount} TL successfully withdrawn. Current balance:{account["balance"]} TL")         
        else:
            print("İnsufficient balance.")   
    else:
        print("the amount to be withdrawn must be positive")        
def balance(account):
    print(f"current balance of the {account["owner"]} account:{account["balance"]} TL")

print("Welcome to our bank account application!  (Access:{get_time()})")
owner=input("Name and surname of the account holder:")
while True:
    entered_pass=input("Please enter your password consisting of 6 digits:")
    if entered_pass.isdigit() and len(entered_pass)==6:
       print("Congratulations! You entered the password correctly.")  
       break 
    else:
       print("Incorrect login! Your password consists of only 6 digits.")
account=create_account(owner)

while(True):
    print("\nOptions:")
    print("1.Deposit Money")
    print("2.Withdraw Money")
    print("3.View Balance")
    print("4.Exit")
    choice=int(input("Make your choice (1-4):"))
    if choice==1:
        amount=float(input("Enter the amount you want to deposit:"))
        deposit(account,amount)
    elif choice==2:
        amount=float(input("Enter the amount you want to withdraw:"))    
        withdraw(account,amount)
    elif choice==3:
        balance(account)    
    elif choice==4:
        print("You are out of the app. Have a nice day!  (Exit:{get_time()})")    
        break
    else:
        print("İnvalid selection. Please make a selection between 1-4. ")
