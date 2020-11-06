import numpy as np

# result = np.array([1,3,5,7,9])

# result = np.arange(1,10)         #.arange(1,10) 1 ile 10 arasındaki sayılardan oluşan bir array oluşturur

# result = np.arange(10,100,3)     # 10 la 100 arasında 3 er 3er artan bir array oluşturur

# result = np.zeros(10)            # .zeros(10) ekrana 10 tane 0 bastırır

# result = np.ones(15)             # . ones(15) ekrana 15 tane 1 bastırır

# result = np.linspace(0,100,5)    # .linspace(0,100,5) 0 ile 100 arasındaki sayıları 5 eşit parçaya böler [  0.  25.  50.  75. 100.]

# result = np.random.randint(0,10,5) # .random.randint(0,10,5) 0 ile 10 arasında 5 tane random sayı üretir

# np_array = np.arange(50)

# np_multi = np_array.reshape(5,10) # 5 e 10 luk bir matris

# print(np_multi.sum(axis=1)) # matris satırları toplamını verir

# print(np_multi.sum(axis=0)) # matris sütunları toplamını verir


rnd_numbers = np.random.randint(1,100,10)

# result = rnd_numbers.max()  # üretilen sayılar içerisinde max olanı verir

result = rnd_numbers.mean()  # üretilen sayılarıın ortalaması verir

print(result)