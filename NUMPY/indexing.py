import numpy as np


numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]  # numbers arrayinde 5. indexteki sayıyı bulur

# print(result)

arr1 = np.arange(1,10)
arr2 = arr1 # referans kopyalaması


arr2[0] = 20

print(arr1)
print(arr2)
