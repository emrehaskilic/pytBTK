sayilar = [1,3,5,7,9,12,19,21]

#1- sayilar listesindeki hangi sayilar 3 ün katıdır?
#2- sayilar listesinde saıların toplamı kaçtır?
#3- sayilar listesindeki tek sayiların karesini alınız


#1
for ucsayi in sayilar:
    if ucsayi % 3 ==0:
        print(ucsayi)
#2
toplam = 0
for sayi in sayilar:
    toplam += sayi
print("toplam:",toplam)

#3
topnum = 0
for num in sayilar:
    if num % 2 == 1:
        topnum += num**2
        print("toplamkareler:",topnum)
        
        

sehirler = ["kocaeli","istanul","ankara","izmir","rize"] 

# 4- Sehirlerden hangisi en fazla 5 karakterlidir?

for sehir in sehirler:
    if len(sehir) < 6:
        print("max 5 karakterli sehirler:",sehir)
              
urunler = [
    {"name":"samsun S6","price":"3000"},
    {"name":"samsun S7","price":"4000"},
    {"name":"samsun S8","price":"5000"},
    {"name":"samsun S9","price":"6000"},
    {"name":"samsun S10","price":"7000"}
          ]              

#5- ürünlerin fiyatının toplamı nedir?     
#6- ürünlerin fiyatından maks 5000 olanları gösteriniz
total = 0
for urun in urunler:
    fiyat = int(urun["price"])
    total += fiyat
    print(total)

#6
for b in urunler:
    fiyat = int(b["price"])  
    if fiyat < 5000:
        print(b["name"],":",b["price"])  
