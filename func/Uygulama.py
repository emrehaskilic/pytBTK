# gönderilen bir kelimeyi belirtilen kez ekrandan gösteren fonsiyonu yazınız

# def yazdir(kelime,adet):
#     print(kelime*adet)

# yazdir("merhaba\n",10)


#2Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonsiyon yazınız

# def listeyeCevir(*params):
#     liste= []

#     for param in params:
#         liste.append(param)
#     return liste
# result = listeyeCevir(10,20,30,"merhaba")  
# print(result)  




# Gönderilen 2 sayı arasındaki tüm asal sayıları bulunuz



# def AsalSayilariBul(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi > 1:
#             for i in range (2,sayi):
#                 if sayi % 1 == 0 :
#                     break
#             else:
#                 print(sayi)    

# sayi1 = int(input("sayi1:"))
# sayi2 = int(input("sayi2:"))

# AsalSayilariBul(sayi1,sayi2)




#kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz

def tamBolenleriBul(sayi):
    tamBolenler = []
    
    for i in range(2,sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)
    return tamBolenler        
print(tamBolenleriBul(20))


