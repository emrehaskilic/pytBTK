
print ( """

**********************
* WELCOME TO E&S BANK*
**********************

        """)


EmreHesap = {


    "İsim":"Emre",
    "Soyisim":" Haskilic",
    "MARS":1,
    "HesapNo": 1,
    "Bakiye": 10000,
    "KMH":20000,
    
            }



SheinaHesap = {


    "İsim":"Sheina",
    "Soyisim":"Haskilic",
    "MARS":2,
    "HesapNo": 2,
    "Bakiye": 10000,
    "KMH":20000,
    
            }

def ParaCek(hesap,miktar):
    print(f"Merhaba {hesap['İsim'] + hesap['Soyisim']}")

    if hesap["Bakiye"] >= miktar:
        print("PARANIZI ALABİLİRSİNİZ")
    else:
        toplam = hesap["Bakiye"] + hesap["KMH"] 

        if toplam >= miktar:
            ekHesapKullanimi = input("Ek hesap kullanilsin mi?(E/H)")
            if ekHesapKullanimi == "E":
                print("Paranızı alabilirsiniz")
            else:
                print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır")    
        else:
            print("Üzgünüz Bakiye Yetersiz")        




ParaCek(EmreHesap,6000)    


