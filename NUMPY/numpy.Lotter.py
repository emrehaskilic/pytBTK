import numpy as np

i = 0
kolonlar = []
while i < 8:

    Kolon = np.random.randint(0,49,6)
    kolonlar.append(Kolon)
    i += 1
for duzenle in kolonlar:

   print(f"""
    -----------------------
    {duzenle}
    -----------------------
         """)