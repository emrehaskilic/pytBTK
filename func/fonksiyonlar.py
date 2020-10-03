def sayHello(name):
    return "Hello" + name
    
msg = sayHello("Emre")

print(msg)

def total(num1,num2):
    return num1 + num2

result = total(10,20)
result = total(15,20)

print(result)

def yashesapla(dogumyili):


    return 2019 - dogumyili

ageEmre = yashesapla(1992)

ageSheina = yashesapla(1988)

print(ageEmre)
print(ageSheina)


def EmekliligeKacYilKaldi(dogumyili,isim):
    yas = yashesapla(dogumyili)
    emeklilik = 65 -yas

    if emeklilik > 0:
        print(f"{isim} Emekliliğinize {emeklilik} yil kaldi")
    else:
        print("Zaten emeklisin")   

EmekliligeKacYilKaldi(1993,"Ali")
EmekliligeKacYilKaldi(1950,"Ali")
EmekliligeKacYilKaldi(1974,"yagmur")


