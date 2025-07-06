import datetime
import json
import os

def get_time():
    return datetime.datetime.now().strftime("%X")

def load_accounts():
    """JSON dosyasından hesapları yükle"""
    if os.path.exists("accounts.json"):
        try:
            with open("accounts.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Hesap dosyası bozuk, yeni dosya oluşturuluyor...")
            return {}
    return {}

def save_accounts(accounts):
    """Hesapları JSON dosyasına kaydet"""
    with open("accounts.json", "w", encoding="utf-8") as file:
        json.dump(accounts, file, ensure_ascii=False, indent=4)

def create_account(accounts, owner_name, password):
    """Yeni hesap oluştur"""
    if owner_name in accounts:
        print(f"❌ {owner_name} adına zaten bir hesap mevcut!")
        return False
    
    accounts[owner_name] = {
        "password": password,
        "balance": 0,
        "created_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_accounts(accounts)
    print(f"✅ {owner_name} adına hesap başarıyla oluşturuldu!")
    return True

def login(accounts, owner_name, password):
    """Hesaba giriş yap"""
    if owner_name not in accounts:
        print("❌ Bu isimde bir hesap bulunamadı!")
        return False
    
    if accounts[owner_name]["password"] != password:
        print("❌ Şifre yanlış!")
        return False
    
    print(f"✅ Hoşgeldiniz {owner_name}!")
    return True

def deposit(accounts, owner_name, amount):
    """Para yatır"""
    if amount > 0:
        accounts[owner_name]["balance"] += amount
        save_accounts(accounts)
        print(f"{amount} TL başarıyla yatırıldı💰. Güncel bakiye: {accounts[owner_name]['balance']} TL")
    else:
        print("Yatırılacak miktar pozitif olmalıdır")

def withdraw(accounts, owner_name, amount):
    """Para çek"""
    if amount > 0:
        if accounts[owner_name]["balance"] >= amount:
            accounts[owner_name]["balance"] -= amount
            save_accounts(accounts)
            print(f"{amount} TL başarıyla çekildi💰. Güncel bakiye: {accounts[owner_name]['balance']} TL")
        else:
            print("Yetersiz bakiye ❌")
    else:
        print("Çekilecek miktar pozitif olmalıdır")

def show_balance(accounts, owner_name):
    """Bakiye göster"""
    print(f"{owner_name} hesabının güncel bakiyesi: {accounts[owner_name]['balance']} TL")

def list_all_accounts(accounts):
    """Tüm hesapları listele (admin özelliği)"""
    if not accounts:
        print("Hiç hesap bulunamadı.")
        return
    
    print("\n=== TÜM HESAPLAR ===")
    for owner, data in accounts.items():
        print(f"İsim: {owner}")
        print(f"Bakiye: {data['balance']} TL")
        print(f"Oluşturulma Tarihi: {data['created_date']}")
        print("-" * 30)

def main():
    accounts = load_accounts()
    
    print(f"🏦 Banka Hesap Uygulamasına Hoşgeldiniz! (Erişim: {get_time()})")
    
    while True:
        print("\n=== ANA MENÜ ===")
        print("1. Yeni Hesap Oluştur")
        print("2. Mevcut Hesaba Giriş Yap")
        print("3. Tüm Hesapları Görüntüle")
        print("4. Uygulamadan Çık")
        
        try:
            main_choice = int(input("Seçiminizi yapın (1-4): "))
        except ValueError:
            print("❌ Geçersiz giriş! Lütfen 1-4 arasında bir sayı girin.")
            continue
        
        if main_choice == 1:
            # Yeni hesap oluştur
            owner = input("Hesap sahibinin adı ve soyadı: ").strip()
            if not owner:
                print("❌ Ad soyad boş olamaz!")
                continue
            
            while True:
                password = input("6 haneli şifrenizi girin: ")
                if password.isdigit() and len(password) == 6:
                    break
                else:
                    print("❌ Şifre sadece 6 haneli rakamlardan oluşmalıdır.")
            
            create_account(accounts, owner, password)
        
        elif main_choice == 2:
            # Mevcut hesaba giriş
            if not accounts:
                print("❌ Henüz hiç hesap oluşturulmamış!")
                continue
            
            owner = input("Hesap sahibinin adı ve soyadı: ").strip()
            password = input("6 haneli şifrenizi girin: ")
            
            if login(accounts, owner, password):
                # Hesap işlemleri menüsü
                while True:
                    print(f"\n=== {owner.upper()} HESAP İŞLEMLERİ ===")
                    print("1. Para Yatır")
                    print("2. Para Çek")
                    print("3. Bakiye Görüntüle")
                    print("4. Ana Menüye Dön")
                    
                    try:
                        choice = int(input("Seçiminizi yapın (1-4): "))
                    except ValueError:
                        print("❌ Geçersiz giriş! Lütfen 1-4 arasında bir sayı girin.")
                        continue
                    
                    if choice == 1:
                        try:
                            amount = float(input("Yatırmak istediğiniz miktarı girin: "))
                            deposit(accounts, owner, amount)
                        except ValueError:
                            print("❌ Geçersiz miktar!")
                    
                    elif choice == 2:
                        try:
                            amount = float(input("Çekmek istediğiniz miktarı girin: "))
                            withdraw(accounts, owner, amount)
                        except ValueError:
                            print("❌ Geçersiz miktar!")
                    
                    elif choice == 3:
                        show_balance(accounts, owner)
                    
                    elif choice == 4:
                        print(f"Ana menüye dönülüyor... (Çıkış: {get_time()})")
                        break
                    
                    else:
                        print("❌ Geçersiz seçim! Lütfen 1-4 arasında bir seçim yapın.")
        
        elif main_choice == 3:
            # Tüm hesapları görüntüle
            list_all_accounts(accounts)
        
        elif main_choice == 4:
            # Uygulamadan çık
            print(f"Uygulamadan çıkılıyor. İyi günler! (Çıkış: {get_time()})")
            break
        
        else:
            print("❌ Geçersiz seçim! Lütfen 1-4 arasında bir seçim yapın.")

if __name__ == "__main__":
    main()
