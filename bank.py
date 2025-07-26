import datetime
import json
import os

def get_time():
    return datetime.datetime.now().strftime("%X")

def load_accounts():
    # JSON dosyasından hesapları yükle
    if os.path.exists("accounts.json"):
        try:
            with open("accounts.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Account file corrupted, creating new file...")
            return {}
    return {}

def save_accounts(accounts):
    # Hesapları JSON dosyasına kaydet
    with open("accounts.json", "w", encoding="utf-8") as file:
        json.dump(accounts, file, ensure_ascii=False, indent=4)

def create_account(accounts, owner_name, password):
    # Yeni hesap oluştur
    if owner_name in accounts:
        print(f"❌ There is already an account in the name of {owner_name}")
        return False
    
    accounts[owner_name] = {
        "password": password,
        "balance": 0,
        "created_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_accounts(accounts)
    print(f"✅ Account on behalf of {owner_name} created successfully")
    return True

def login(accounts, owner_name, password):
    # Hesaba giriş yap
    if owner_name not in accounts:
        print("❌ No account with this name found!")
        return False
    
    if accounts[owner_name]["password"] != password:
        print("❌ Password is incorrect!")
        return False
    
    print(f"✅ Welcome {owner_name}!")
    return True

def confirm_transaction(transaction_type, amount, owner_name, current_balance=None):
    """
    Transaction confirmation function
    transaction_type: "deposit" or "withdraw"
    amount: transaction amount
    owner_name: account holder name
    current_balance: current balance (for withdraw transaction)
    """
    print("\n" + "="*50)
    print("🔍 TRANSACTION CONFIRMATION")
    print("="*50)
    
    if transaction_type == "deposit":
        print(f"💰 Money Deposit Transaction")
        print(f"👤 Account Holder: {owner_name}")
        print(f"💵 Amount to Deposit: {amount} TL")
    
    elif transaction_type == "withdraw":
        print(f"🏧 Money Withdrawal Transaction")
        print(f"👤 Account Holder: {owner_name}")
        print(f"💵 Amount to Withdraw: {amount} TL")
        if current_balance is not None:
            print(f"💳 Current Balance: {current_balance} TL")
            print(f"💳 Balance After Transaction: {current_balance - amount} TL")
    
    print("="*50)
    
    while True:
        confirmation = input("Do you confirm this transaction? (yes/y or no/n): ").strip().lower()
        
        if confirmation in ['yes', 'y']:
            print("✅ Transaction confirmed!")
            return True
        elif confirmation in ['no', 'n']:
            print("❌ Transaction cancelled!")
            return False
        else:
            print("❌ Invalid input! Please enter 'yes' or 'no'.")

def deposit(accounts, owner_name, amount):
    # Deposit money - with confirmation
    if amount <= 0:
        print("The amount to be deposited must be positive")
        return
    
    # Transaction confirmation
    if confirm_transaction("deposit", amount, owner_name):
        accounts[owner_name]["balance"] += amount
        save_accounts(accounts)
        print(f"{amount} TL successfully deposited💰. Current balance: {accounts[owner_name]['balance']} TL")
    else:
        print("🔄 Returning to main menu...")

def withdraw(accounts, owner_name, amount):
    # Withdraw money - with confirmation
    if amount <= 0:
        print("The amount to be withdrawn must be positive")
        return
    
    current_balance = accounts[owner_name]["balance"]
    
    if current_balance < amount:
        print("insufficient balance ❌")
        return
    
    # Transaction confirmation
    if confirm_transaction("withdraw", amount, owner_name, current_balance):
        accounts[owner_name]["balance"] -= amount
        save_accounts(accounts)
        print(f"{amount} TL successfully withdrawn💰. Current balance: {accounts[owner_name]['balance']} TL")
    else:
        print("🔄 Returning to main menu...")

def show_balance(accounts, owner_name):
    # Show balance
    print(f"current balance of the {owner_name} account: {accounts[owner_name]['balance']} TL")

def list_all_accounts(accounts):
    # List all accounts
    if not accounts:
        print("No accounts found.")
        return
    
    print("\n=== ALL ACCOUNTS ===")
    for owner, data in accounts.items():
        print(f"Name: {owner}")
        print(f"Balance: {data['balance']} TL")
        print(f"Creation date: {data['created_date']}")
        print("-" * 30)

def main():
    accounts = load_accounts()
    
    print(f"🏦 Welcome to Bank Account App! (Access: {get_time()})")
    
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Create new account")
        print("2. Login to Existing Account")
        print("3. View All Accounts")
        print("4. Exit Application")
        
        try:
            main_choice = int(input("enter your choice (1-4): "))
        except ValueError:
            print("❌ Invalid input! Please enter a number between 1-4.")
            continue
        
        if main_choice == 1:
            # Create new account
            owner = input("Name and surname of the account holder: ").strip()
            if not owner:
                print("❌ Name and surname cannot be empty!")
                continue
            
            while True:
                password = input("Enter your 6-digit password: ")
                if password.isdigit() and len(password) == 6:
                    break
                else:
                    print("❌ The password must consist of 6 digits only.")
            
            create_account(accounts, owner, password)
        
        elif main_choice == 2:
            # Login to existing account
            if not accounts:
                print("❌ No accounts created yet!")
                continue
            
            owner = input("Name and surname of the account holder: ").strip()
            password = input("Enter your 6-digit password: ")
            
            if login(accounts, owner, password):
                # Account operations menu
                while True:
                    print(f"\n=== {owner.upper()} ACCOUNT PROCESSING ===")
                    print("1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. View Balance")
                    print("4. Back to Main Menu")
                    
                    try:
                        choice = int(input("enter your choice (1-4): "))
                    except ValueError:
                        print("❌ Invalid input! Please enter a number between 1-4.")
                        continue
                    
                    if choice == 1:
                        try:
                            amount = float(input("Enter the amount you want to deposit: "))
                            deposit(accounts, owner, amount)
                        except ValueError:
                            print("❌ Invalid amount!")
                    
                    elif choice == 2:
                        try:
                            amount = float(input("Enter the amount you want to withdraw: "))
                            withdraw(accounts, owner, amount)
                        except ValueError:
                            print("❌ Invalid amount!")
                    
                    elif choice == 3:
                        show_balance(accounts, owner)
                    
                    elif choice == 4:
                        print(f"Returning to main menu... (Exit: {get_time()})")
                        break
                    
                    else:
                        print("❌ Invalid input! Please enter a number between 1-4.")
        
        elif main_choice == 3:
            # View all accounts
            list_all_accounts(accounts)
        
        elif main_choice == 4:
            # Exit application
            print(f"Exiting the application. Have a nice day! (Exit: {get_time()})")
            break
        
        else:
            print("❌ Invalid input! Please enter a number between 1-4.")

if __name__ == "__main__":
    main()
