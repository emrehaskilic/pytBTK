harfler = [
    
        {"deger":"İSİM", "harf":"EMRE"},
        {"deger":"SOYİSİM", "harf":"a"},
        {"deger":"TEL", "harf":"TEADAS"},
        
]

# deger = input("deger:")
# harf = input("harf")

for i in harfler:
    deger = input(i["deger"])
    harf = input(i["harf"])
    i.update({

            "deger":deger,
             "harf":harf

    })
print(harfler)



# harfler.update({

#         "deger":deger,
#         "harf":harf
#                  }
#                   )
# print(harfler)                  



