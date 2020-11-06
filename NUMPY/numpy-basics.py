import numpy as np

# numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9])

np_multi = np_array.reshape(3,3) # TEK BOYUTLU BİR ARRAY'I 3 E 3 LÜK BİR MATRİSE DÖNÜŞTÜRÜR

print(np_multi)

print(np_multi.ndim) # .ndim => boyut gösterir

print(np_array.shape) # .shape => boyut gösterir çıktı = (9,)
print(np_multi.shape) # çıktı = (3,3)



