# def fibonachi(n):
#     sonlar = []
#     for i in range(n):
#         if i == 0 or i == 1:
#             sonlar.append(1)   # 1 1
#         else:
#             sonlar.append(sonlar[i-1] + sonlar[i-2])
        
#     return sonlar

# print(fibonachi(12))



# Funksiyalar --> so'ngi mavzu
# lambda  --> nomsiz funksiya 

# PI = 3.14

# uzunlik = lambda pi, r: 2*pi*r # ifoda doim 1 ta bo'lishi kerak

# print(uzunlik(PI, 4))


kvadrat = lambda x: x**2
# print(kvadrat(3))

# daraja = lambda x, y: x**y

# print(daraja(3, 4))




# map --> royxat elementlariga ishlov berish

# sonlar = [3, 5, 2, 7]

# kvadratlar = list(map(kvadrat, sonlar))

# print(kvadratlar)


# sonlar = [3, 5, 2, 7]
# kvadratlar = list(map(lambda x: x**2, sonlar))
# print(kvadratlar)

# qoshish = list(map(lambda x,y: x+y, [12, 3, 4], [3, 5, 6]))

# print(qoshish)



# filter --> True yoki False qaytaradigan funksiya asosida royxat elementlarini filterlaydi

# sonlar = [12, 42, 2, 5, 7, 33]

# juft_sonlar = list(filter(lambda son: son%2==0, sonlar))

# print(juft_sonlar)

# mevalar = ['olma', 'anor', 'behi', 'apelsin', 'ananas', 'banan']

# f_mevalar = list(filter(lambda s: len(s)<=4, mevalar))

# print(f_mevalar)


# mevalar = ['olma', 'anor', 'behi', 'apelsin', 'ananas', 'banan']

# f_mevalar = list(filter(lambda s: s.startswith('a') and s.endswith('s') , mevalar))

# print(f_mevalar)

# UYGA VAZIFA
# Son topish o'yini: 
# Kompyuter taxminiy son o'ylaydi foydalanuvchi uni bir nechta urinishda topadi,
# Keyin foydalanuvchi son o'ylaydi kompyuter uni bir nechta urinishda topadi.
# Agar kim kam urinishda topsa o'sha g'olib
