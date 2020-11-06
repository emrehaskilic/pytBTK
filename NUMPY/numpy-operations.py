import numpy as np

numbers1 = np.random.randint(10,100,6)

numbers2 = np.random.randint(10,100,6)

print(numbers1) # [89 33 90 17 10 73]
print(numbers2) # [13 52 82 57 59 29]

# result = numbers1 + numbers2 # 2 arrayın aynı indexte olan sayıları toplandı / [102  85 172  74  69 102]
# result = numbers1 + 100 # numbers 1 arrayındeki her değeri 100 ile toplad
# result = numbers1 - numbers2 # 2 arrayın aynı indexte olan elemanları arasında çıkarma işlemi yapar
# result = numbers1 * numbers2 # çarpma işlemi

# result = np.sin(numbers1) # numbers1 in sinüsünü alır

# result = np.sqrt(numbers1) # numbers1 in her bir elemanının karekökünü alır

# result = np.log(numbers1)  # numbes 1 in her bir elemanının logaritmasını alır


mnumbers1 = numbers1.reshape(2,3)

mnumbers2 = numbers2.reshape(2,3)

print(mnumbers1)
print(mnumbers2)

result = np.vstack((mnumbers1,mnumbers2)) # matrisleri dikey olarak birleştirir
result = np.hstack((mnumbers1,mnumbers2)) # matrisleri yatay olarak birleştirir




print(result)



