import datetime
def get_time():
    return datetime.datetime.now().strftime("%X")
def create_account(owner_name):
    return {"owner":owner_name,"balance":0}
def yatırma(account,amount):
    if amount>0:
        account["balance"]+=amount    
        print(f"{amount} TL başarılı bir şekilde yatırıldı. güncel bakiyeniz:{account["balance"]} TL")
    else:
        print("yatırılacak miktar pozitif olmalı")
def çekme(account,amount):
    if amount>0:
        if account["balance"]>=amount:
           account["balance"]-=amount
           print(f"{amount} TL başarılı bir şekilde çekildi. güncel bakiyeniz:{account["balance"]} TL")         
        else:
            print("yetersiz bakiye.")   
    else:
        print("çekilecek miktar pozitif olmalı")        
def balance(account):
    print(f"{account["owner"]} hesabının güncel bakiyesi:{account["balance"]} TL")

print("bankamızın hesap uygulamasına hoş geldiniz!  (Giriş:{get_time()})")
owner=input("hesap sahibinin adı:")
while True:
    entered_pass=input("Lütfen 6 haneli rakamlardan oluşan şifrenizi giriniz:")
    if entered_pass.isdigit() and len(entered_pass)==6:
       print("tebrikler şifreyi doğru girdiniz.")  
       break 
    else:
       print("Hatalı giriş! şifreniz sadece 6 haneli rakamlardan oluşmaktadır.")
account=create_account(owner)

while(True):
    print("\nseçenekler:")
    print("1.para yatır")
    print("2.para çek")
    print("3.bakiye görüntüle")
    print("4.çıkış")
    choice=int(input("seçiminizi yapınız (1-4):"))
    if choice==1:
        amount=float(input("yatırmak istediğiniz miktarı giriniz:"))
        yatırma(account,amount)
    elif choice==2:
        amount=float(input("çekmek istediğiniz miktarı giriniz:"))    
        çekme(account,amount)
    elif choice==3:
        balance(account)    
    elif choice==4:
        print("uygulamadan çıktınız. iyi günler dileriz  (Çıkış:{get_time()})")    
        break
    else:
        print("geçersiz seçim.lütfen 1-4 arasında bir seçim yapınız ")
