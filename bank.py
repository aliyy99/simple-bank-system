import datetime
import json
import os

# Basit çeviri sözlüğü - Sadece temel kelimeler
TRANSLATIONS = {
    "en": {
        "name": "English",
        "yes": ["yes", "y"],
        "no": ["no", "n"]
    },
    "tr": {
        "name": "Türkçe", 
        "yes": ["evet", "e"],
        "no": ["hayır", "h"]
    },
    "fr": {
        "name": "Français",
        "yes": ["oui", "o"], 
        "no": ["non", "n"]
    },
    "de": {
        "name": "Deutsch",
        "yes": ["ja", "j"],
        "no": ["nein", "n"]
    },
    "es": {
        "name": "Español",
        "yes": ["sí", "si", "s"],
        "no": ["no", "n"]
    }
}

# Kelime bazlı çeviri sözlüğü
WORD_DICT = {
    "Bank": {"en": "Bank", "tr": "Banka", "fr": "Banque", "de": "Bank", "es": "Banco"},
    "Account": {"en": "Account", "tr": "Hesap", "fr": "Compte", "de": "Konto", "es": "Cuenta"},
    "Welcome": {"en": "Welcome", "tr": "Hoş Geldiniz", "fr": "Bienvenue", "de": "Willkommen", "es": "Bienvenido"},
    "Menu": {"en": "Menu", "tr": "Menü", "fr": "Menu", "de": "Menü", "es": "Menú"},
    "Create": {"en": "Create", "tr": "Oluştur", "fr": "Créer", "de": "Erstellen", "es": "Crear"},
    "Login": {"en": "Login", "tr": "Giriş", "fr": "Connexion", "de": "Anmelden", "es": "Iniciar"},
    "View": {"en": "View", "tr": "Görüntüle", "fr": "Voir", "de": "Anzeigen", "es": "Ver"},
    "Exit": {"en": "Exit", "tr": "Çıkış", "fr": "Sortir", "de": "Beenden", "es": "Salir"},
    "Name": {"en": "Name", "tr": "İsim", "fr": "Nom", "de": "Name", "es": "Nombre"},
    "Password": {"en": "Password", "tr": "Şifre", "fr": "Mot de passe", "de": "Passwort", "es": "Contraseña"},
    "Balance": {"en": "Balance", "tr": "Bakiye", "fr": "Solde", "de": "Kontostand", "es": "Saldo"},
    "Deposit": {"en": "Deposit", "tr": "Para Yatır", "fr": "Dépôt", "de": "Einzahlen", "es": "Depositar"},
    "Withdraw": {"en": "Withdraw", "tr": "Para Çek", "fr": "Retirer", "de": "Abheben", "es": "Retirar"},
    "Money": {"en": "Money", "tr": "Para", "fr": "Argent", "de": "Geld", "es": "Dinero"},
    "Transaction": {"en": "Transaction", "tr": "İşlem", "fr": "Transaction", "de": "Transaktion", "es": "Transacción"},
    "Confirmation": {"en": "Confirmation", "tr": "Doğrulama", "fr": "Confirmation", "de": "Bestätigung", "es": "Confirmación"},
    "Success": {"en": "Success", "tr": "Başarılı", "fr": "Succès", "de": "Erfolgreich", "es": "Éxito"},
    "Error": {"en": "Error", "tr": "Hata", "fr": "Erreur", "de": "Fehler", "es": "Error"},
    "Invalid": {"en": "Invalid", "tr": "Geçersiz", "fr": "Invalide", "de": "Ungültig", "es": "Inválido"},
    "Application": {"en": "Application", "tr": "Uygulama", "fr": "Application", "de": "Anwendung", "es": "Aplicación"},
    "Current": {"en": "Current", "tr": "Mevcut", "fr": "Actuel", "de": "Aktuell", "es": "Actual"},
    "Amount": {"en": "Amount", "tr": "Miktar", "fr": "Montant", "de": "Betrag", "es": "Cantidad"},
    "Holder": {"en": "Holder", "tr": "Sahibi", "fr": "Titulaire", "de": "Inhaber", "es": "Titular"},
    "Created": {"en": "Created", "tr": "Oluşturuldu", "fr": "Créé", "de": "Erstellt", "es": "Creado"},
    "Found": {"en": "Found", "tr": "Bulundu", "fr": "Trouvé", "de": "Gefunden", "es": "Encontrado"},
    "Incorrect": {"en": "Incorrect", "tr": "Yanlış", "fr": "Incorrect", "de": "Falsch", "es": "Incorrecto"},
    "Empty": {"en": "Empty", "tr": "Boş", "fr": "Vide", "de": "Leer", "es": "Vacío"},
    "Positive": {"en": "Positive", "tr": "Pozitif", "fr": "Positif", "de": "Positiv", "es": "Positivo"},
    "Insufficient": {"en": "Insufficient", "tr": "Yetersiz", "fr": "Insuffisant", "de": "Unzureichend", "es": "Insuficiente"},
    "Cancelled": {"en": "Cancelled", "tr": "İptal", "fr": "Annulé", "de": "Abgebrochen", "es": "Cancelado"},
    "Confirmed": {"en": "Confirmed", "tr": "Onaylandı", "fr": "Confirmé", "de": "Bestätigt", "es": "Confirmado"},
    "Returning": {"en": "Returning", "tr": "Dönülüyor", "fr": "Retour", "de": "Zurückkehren", "es": "Regresando"}
}

# Global değişkenler
current_language = "en"

def select_language():
    """Dil seçimi fonksiyonu"""
    global current_language
    
    print("\n" + "="*50)
    print("Please select your language / Lütfen dilinizi seçin")
    print("="*50)
    
    for i, (lang_code, lang_data) in enumerate(TRANSLATIONS.items(), 1):
        print(f"{i}. {lang_data['name']} ({lang_code.upper()})")
    
    print("="*50)
    
    while True:
        try:
            choice = int(input("Select (1-5): "))
            if 1 <= choice <= 5:
                lang_codes = list(TRANSLATIONS.keys())
                current_language = lang_codes[choice - 1]
                print(f"✅ {t('Language')}: {TRANSLATIONS[current_language]['name']}")
                break
            else:
                print("❌ Invalid choice!")
        except ValueError:
            print("❌ Invalid input!")

def t(word):
    """Kelime çevirisi fonksiyonu"""
    return WORD_DICT.get(word, {}).get(current_language, word)

def get_confirmation_words():
    """Onay kelimelerini al"""
    return TRANSLATIONS[current_language]["yes"], TRANSLATIONS[current_language]["no"]

def get_time():
    return datetime.datetime.now().strftime("%X")

def load_accounts():
    if os.path.exists("accounts.json"):
        try:
            with open("accounts.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Account file corrupted, creating new file...")
            return {}
    return {}

def save_accounts(accounts):
    with open("accounts.json", "w", encoding="utf-8") as file:
        json.dump(accounts, file, ensure_ascii=False, indent=4)

def create_account(accounts, owner_name, password):
    if owner_name in accounts:
        print(f"❌ There is already an {t('Account').lower()} in the name of {owner_name}")
        return False
    
    accounts[owner_name] = {
        "password": password,
        "balance": 0,
        "created_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_accounts(accounts)
    print(f"✅ {t('Account')} on behalf of {owner_name} {t('Created').lower()} successfully")
    return True

def login(accounts, owner_name, password):
    if owner_name not in accounts:
        print(f"❌ No {t('Account').lower()} with this name {t('Found').lower()}!")
        return False
    
    if accounts[owner_name]["password"] != password:
        print(f"❌ {t('Password')} is {t('Incorrect').lower()}!")
        return False
    
    print(f"✅ {t('Welcome')} {owner_name}!")
    return True

def confirm_transaction(transaction_type, amount, owner_name, current_balance=None):
    print("\n" + "="*50)
    print(f"🔍 {t('Transaction').upper()} {t('Confirmation').upper()}")
    print("="*50)
    
    if transaction_type == "deposit":
        print(f"💰 {t('Money')} {t('Deposit')} {t('Transaction')}")
        print(f"👤 {t('Account')} {t('Holder')}: {owner_name}")
        print(f"💵 {t('Amount')} to {t('Deposit')}: {amount} TL")
    
    elif transaction_type == "withdraw":
        print(f"🏧 {t('Money')} {t('Withdraw')} {t('Transaction')}")
        print(f"👤 {t('Account')} {t('Holder')}: {owner_name}")
        print(f"💵 {t('Amount')} to {t('Withdraw')}: {amount} TL")
        if current_balance is not None:
            print(f"💳 {t('Current')} {t('Balance')}: {current_balance} TL")
            print(f"💳 {t('Balance')} After {t('Transaction')}: {current_balance - amount} TL")
    
    print("="*50)
    
    yes_words, no_words = get_confirmation_words()
    
    while True:
        confirmation = input(f"Do you confirm this {t('Transaction').lower()}? ({'/'.join(yes_words)} or {'/'.join(no_words)}): ").strip().lower()
        
        if confirmation in yes_words:
            print(f"✅ {t('Transaction')} {t('Confirmed').lower()}!")
            return True
        elif confirmation in no_words:
            print(f"❌ {t('Transaction')} {t('Cancelled').lower()}!")
            return False
        else:
            print(f"❌ {t('Invalid')} input!")

def deposit(accounts, owner_name, amount):
    if amount <= 0:
        print(f"The {t('Amount').lower()} to be deposited must be {t('Positive').lower()}")
        return
    
    if confirm_transaction("deposit", amount, owner_name):
        accounts[owner_name]["balance"] += amount
        save_accounts(accounts)
        print(f"{amount} TL successfully deposited💰. {t('Current')} {t('Balance').lower()}: {accounts[owner_name]['balance']} TL")
    else:
        print(f"🔄 {t('Returning')} to main {t('Menu').lower()}...")

def withdraw(accounts, owner_name, amount):
    if amount <= 0:
        print(f"The {t('Amount').lower()} to be withdrawn must be {t('Positive').lower()}")
        return
    
    current_balance = accounts[owner_name]["balance"]
    
    if current_balance < amount:
        print(f"{t('Insufficient').lower()} {t('Balance').lower()} ❌")
        return
    
    if confirm_transaction("withdraw", amount, owner_name, current_balance):
        accounts[owner_name]["balance"] -= amount
        save_accounts(accounts)
        print(f"{amount} TL successfully withdrawn💰. {t('Current')} {t('Balance').lower()}: {accounts[owner_name]['balance']} TL")
    else:
        print(f"🔄 {t('Returning')} to main {t('Menu').lower()}...")

def show_balance(accounts, owner_name):
    print(f"{t('Current').lower()} {t('Balance').lower()} of the {owner_name} {t('Account').lower()}: {accounts[owner_name]['balance']} TL")

def list_all_accounts(accounts):
    if not accounts:
        print(f"No {t('Account').lower()}s {t('Found').lower()}.")
        return
    
    print(f"\n=== ALL {t('Account').upper()}S ===")
    for owner, data in accounts.items():
        print(f"{t('Name')}: {owner}")
        print(f"{t('Balance')}: {data['balance']} TL")
        print(f"{t('Create')} date: {data['created_date']}")
        print("-" * 30)

def main():
    select_language()
    
    accounts = load_accounts()
    
    print(f"\n🏦 {t('Welcome')} to {t('Bank')} {t('Account')} {t('Application')}! (Access: {get_time()})")
    
    while True:
        print(f"\n=== MAIN {t('Menu').upper()} ===")
        print(f"1. {t('Create')} new {t('Account').lower()}")
        print(f"2. {t('Login')} to Existing {t('Account')}")
        print(f"3. {t('View')} All {t('Account')}s")
        print(f"4. {t('Exit')} {t('Application')}")
        print(f"5. Change Language / Dil Değiştir")
        
        try:
            main_choice = int(input("enter your choice (1-5): "))
        except ValueError:
            print(f"❌ {t('Invalid')} input! Please enter a number between 1-5.")
            continue
        
        if main_choice == 1:
            owner = input(f"{t('Name')} and surname of the {t('Account').lower()} {t('Holder').lower()}: ").strip()
            if not owner:
                print(f"❌ {t('Name')} and surname cannot be {t('Empty').lower()}!")
                continue
            
            while True:
                password = input(f"Enter your 6-digit {t('Password').lower()}: ")
                if password.isdigit() and len(password) == 6:
                    break
                else:
                    print(f"❌ The {t('Password').lower()} must consist of 6 digits only.")
            
            create_account(accounts, owner, password)
        
        elif main_choice == 2:
            if not accounts:
                print(f"❌ No {t('Account').lower()}s {t('Created').lower()} yet!")
                continue
            
            owner = input(f"{t('Name')} and surname of the {t('Account').lower()} {t('Holder').lower()}: ").strip()
            password = input(f"Enter your 6-digit {t('Password').lower()}: ")
            
            if login(accounts, owner, password):
                while True:
                    print(f"\n=== {owner.upper()} {t('Account').upper()} PROCESSING ===")
                    print(f"1. {t('Deposit')} {t('Money')}")
                    print(f"2. {t('Withdraw')} {t('Money')}")
                    print(f"3. {t('View')} {t('Balance')}")
                    print(f"4. Back to Main {t('Menu')}")
                    
                    try:
                        choice = int(input("enter your choice (1-4): "))
                    except ValueError:
                        print(f"❌ {t('Invalid')} input! Please enter a number between 1-4.")
                        continue
                    
                    if choice == 1:
                        try:
                            amount = float(input(f"Enter the {t('Amount').lower()} you want to {t('Deposit').lower()}: "))
                            deposit(accounts, owner, amount)
                        except ValueError:
                            print(f"❌ {t('Invalid')} {t('Amount').lower()}!")
                    
                    elif choice == 2:
                        try:
                            amount = float(input(f"Enter the {t('Amount').lower()} you want to {t('Withdraw').lower()}: "))
                            withdraw(accounts, owner, amount)
                        except ValueError:
                            print(f"❌ {t('Invalid')} {t('Amount').lower()}!")
                    
                    elif choice == 3:
                        show_balance(accounts, owner)
                    
                    elif choice == 4:
                        print(f"{t('Returning')} to main {t('Menu').lower()}... ({t('Exit')}: {get_time()})")
                        break
                    
                    else:
                        print(f"❌ {t('Invalid')} input! Please enter a number between 1-4.")
        
        elif main_choice == 3:
            list_all_accounts(accounts)
        
        elif main_choice == 4:
            print(f"Exiting the {t('Application').lower()}. Have a nice day! ({t('Exit')}: {get_time()})")
            break
        
        elif main_choice == 5:
            select_language()
        
        else:
            print(f"❌ {t('Invalid')} input! Please enter a number between 1-5.")

if __name__ == "__main__":
    main()
