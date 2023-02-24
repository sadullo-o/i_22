# UYGA VAZIFA KODI

# sonlar = list(range(15, -16, -1))
# print(sonlar)

# Ro'yxatdan ko'chirib olish
# sonlar = [12, 53, 44, 98, 120, 4, 55, 17, 32]
# yangi_sonlar = sonlar[2:5] # 2-indeksdan 4-indeksgacha ko'chirib oladi
# print(yangi_sonlar)
# print(sonlar)

# yangi_sonlar = sonlar[:5] # boshidan ko'chirib oladi
# print(yangi_sonlar)

# yangi_sonlar = sonlar[2:]
# print(yangi_sonlar)

# sonlar2 = sonlar
# sonlar2[0] = 777
# print(sonlar)

# sonlar2 = sonlar[:]  # to'liq ko'chirib olish
# sonlar2[0] = 777
# print(sonlar2)

# sonlar2 = sonlar.copy() # to'liq ko'chirib olish
# sonlar2[0] = 222
# print(sonlar)

# list()
# sonlar2 = list(sonlar) # to'liq ko'chirib olish
# sonlar2[0] = 222
# print(sonlar2)



# Ro'yxatlarni qo'shish

# royxatlarni qo'shib boshqa royxat yaratish
# cars = ['nexia', 'cobalt', 'lacetti']
# cars2 = ['damas', 'malibu', 'jentra']
# allcars = cars2 + cars
# print(allcars)

# extend()  --> bir royxatga boshqa royxatni qo'shib olish
# cars = ['nexia', 'cobalt', 'lacetti']
# cars2 = ['damas', 'malibu', 'jentra']
# cars.extend(cars2)
# print(cars)
# print(cars2)


#element nechi marta takrorlanganini sanaydi  royxat.count(qiymat)
# cars = ['nexia', 'cobalt', 'lacetti', 'nexia', 'nexia']
# print(cars.count('nexia'))


# Royxatni tozalash
# cars = ['nexia', 'cobalt', 'lacetti', 'nexia', 'nexia']
# cars.clear()
# print(cars)

# amaliy mashq --> 100 - 800 gacha juft sonlar royxati yaratilsin
#  va boshidan 20 ta o'rtasidan 20 ta va oxiridan 20 ta ko'chirib olinsin



# O'zgarmas ro'yxat -- Tuple  
# mevalar = ('olma', 'anor', 'behi', 'nok', 'anor')

# print(mevalar[2])
# mevalar[1] = 'banan' # xato

# # list() --> boshqa ketma ketlik yoki royxatlarni list turiga o'tkazish
# l_mevalar = list(mevalar)
# l_mevalar[1] = 'banan'

# # tuple() --> boshqa ketma ketlik yoki royxatlarni tuple turiga o'tkazish
# mevalar = tuple(l_mevalar)
# print(mevalar)

# o'zgaruvchilarga bo'lishimiz mumkin
# (meva1, meva2, meva3, meva4) = mevalar
# print(meva1)
# print(meva2)
# print(meva3)
# print(meva4)


# tuple ni ko'paytirish
# print(mevalar * 2)

# print(mevalar.count('anor'))




# Set  --> royxat turi, bu tartiblanmagan lekin element qo'shish mumkin yoki set ni o'zgartirish mumkin

# mevalar = {'olma', 'anor', 'behi', 'nok'}
# mevalar2 = {'ananas', 'kivi'}

# mevalar.add('banan')
# print(mevalar)

# r = list(mevalar)
# print(r)

# mevalar2.update(mevalar)
# print(mevalar2)


# mevalar2 = ('ananas', 'kivi')

# mevalar.update(mevalar2)
# print(mevalar)


# elementlarni o'chirish
# mevalar.remove('anor')
# print(mevalar)
# mevalar.discard('olma')
# print(mevalar)


# a = mevalar.pop()
# print(mevalar)
# print(a)


# mevalar.clear()
# print(mevalar)

# del mevalar
# print(mevalar)



# mevalar = {'olma', 'anor', 'behi', 'nok'}
# mevalar2 = {'ananas', 'kivi', 'behi', 'olma'}


# mevalar3 = mevalar.union(mevalar2)

# print(mevalar3)

# a = mevalar.difference(mevalar2)
# print(a)

# users = ['ali', 'vali']
# users = ('ali', 'vali')

# tuple yaratib uni ichidan elementni o'chirilsin.

# cities = ('Buxoro', 'Toshkent', 'Andijon')
# cities = list(cities)
# cities.remove('Andijon')
# cities = tuple(cities)
# print(cities)


#
# x = 5
# y = 6
# x, y = y, x
# print(x)
# print(y)



# UYGA VAZIFA
# 1. Foydalanuvchidan son so'rab u sonni kvadrati, kubi, to'rtinchi darajasini
# royxat qilib print qilish
# 2. Foydalanuvchidan 3 ta ism so'rab uni bo'sh set ga qo'shish
# 3. Foydalanuvchidan 2 ta son so'rab a sonni b darajasini hisoblab berish

# 1 vazifa
# son = int(input('Sonni kiriting: '))

# natijalar = []

# natijalar.append(son**2)
# natijalar.append(son**3)
# natijalar.append(son**4)
# print(natijalar)


# 2 vazifa

# ismlar = {}
# ismlar = set(ismlar)
# ism1 = input('Ism kiriting: ')
# ism2 = input('Ism kiriting: ')
# ism3 = input('Ism kiriting: ')
# ismlar.add(ism1)
# ismlar.add(ism2)
# ismlar.add(ism3)
# print(ismlar)

# 3 vazifa

# son1 = int(input('1-sonni kiriting: '))
# son2 = int(input('2-sonni kiriting: '))
# print(son1**son2)