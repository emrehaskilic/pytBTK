# # def changeName(n):
# #     n = "ada"
# # name = "yiğit"    

# # changeName(name)

# # print(name)

# # def change(n):
# #     n[0] = "istanbul"

# # sehirler = ["ankara","izmir"]
# # change(sehirler[:])

# # print(sehirler)

# def add(*params):
#     print(params[0])
#     return sum((params))

# print(add(10,20))

# print(add(10,20,30,50,100))

def displayUser(**args)  :
    for key,value in args.items():
        print("{}:{}".format(key,value))
displayUser(name="Çınar", age = 2, city = "İstanbul")
displayUser(name="Ada", age = 12, city = "koaceli",phone = "12")
displayUser(name="yiğit", age = 14, city = "ankara",phone = "12",email = "yigit@gmail.com")

myfunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myfunc(10,20,30,40,50, key1 = "value1", key2 = "value2")    





