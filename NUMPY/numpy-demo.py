import numpy as np
# 1) (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.
sonuc = np.array([15,15,30,45,60])
print(sonuc)

# 2) (5-15) arasındaki sayılarla bir numpy dizisi oluşturunuz.
a = np.arange(5,15)
print(a)

# 3) (50-100) arasında 5'er 5'er artan bir numpy dizisi oluşturun.
b = np.arange(50,100,5)
print(b)    

# 4) 10 elemanlı 0 lardan oluşan bir numpy dizisi oluşturunuz.

c = np.zeros(10)
print(c)

# 5) 10 elemanlı 1 lerden oluşan bir numpy dizisi oluşturunuz.
d = np.ones(10)
print(d)

# 6) (10-30) arasında rastgele 5 tam sayi üretiniz
e = np.random.randint(10,30,5)
print(f"***{e}***")

# 7) (0-100) arasında eşit aralıklı 5 sayı üretin
f = np.linspace(0,100,5)
print(f)

# 8) [-1 ile 1] arasında 10 adet sayı üretin
g = np.random.randn(10)
print(g)

# 9) (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz
h = np.random.randint(10,50,15).reshape(3,5)
print(h)

# 10) Üretilen matrisin satır ve sütünlarının toplamını hesaplayınız.
sutun_toplam = h.sum(axis=1)
satir_toplam = h.sum(axis=0)
print(f"Sütunların Toplamı : {sutun_toplam}\nSatırların Toplamı : {satir_toplam}")

# 11) Üretilen Matrisin en büyük,enküçük ve ortalaması nedir.
max = h.max()
min = h.min()
ort = h.mean()
print(f"Max değer : {max}\nMin değer : {min}\nOrtalama değer : {ort}")

# 12) Üretilen matrisin en büyük ve en küçük değerinin indeksleri kaçtır?
print(f"Üretilen Matrisin En Büyük Değerinin İndexi : {h.argmax()}\nÜretilen Matrisin En Büyük Değerinin İndexi : {h.argmin()}")

# 13) (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.
arr = np.arange(10,20)
print(f"{arr} ve {arr[0:3]}")

# 15) Üretilen Matrisin ilk satırını seçiniz.
g = h[0]
print(g)

# 16 ) Üretilen Matrisin 2. satırının 3. sütunundaki elemanı seçiniz
print(f"Matrisin 2. satır 3. sütun elemanı {h[1,2]}")

# 17) Matrisin tüm satırlarının ilk elemanlarını seçiniz
print(f"Matrisin tüm satırlarının ilk elemanı{h[:,0]}")

# 18) Üretilen matrisin her bir elemanın karesini alınız
print(f"Matris elemanlarının karesi :{h**2}")

# 19) Üretilen matris elemanlarının hangisi pozitif çift sayıdır.
    # aralık (-50,50)
result = h % 2 == 0



