# UYGA VAZIFA
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# print(ismlar[0].capitalize(), ' qachon kelasan!')
# print('Salom ', ismlar[1].title(), ' yaxshimisan')

# sonlar = [13, -7, 4.3, -12.8]
# print(sonlar[1] + sonlar[3])
# print(sonlar[0]**2)
# print(sonlar[3]- sonlar[1])

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', "Rustam"]
# kelganlar = []

# kelganlar.append(mehmonlar.pop(1))
# kelganlar.append(mehmonlar.pop(3))
# kelganlar.append(mehmonlar.pop(-1))

# print(kelganlar)
# print(mehmonlar)


# shaharlar = ['Buxoro', 'Toshkent', 'Jizzax']

# shaharlar.append('Samarqand')

# shaharlar.insert(0, 'Andijon')

# shaharlar.insert(2, 'Navoiy')
# print(shaharlar)



# Ro'yxatlar bilan ishlash
# royxatni tartiblash sort()

mevalar = ['olma', 'Anor', 'behi', 'nok', 'anjir' ,'Uzum']
# tartiblashda doim bosh harflar birinchi tartiblanadi undan 
# keyin kichik harflarga navbat keladi
# mevalar.sort() # sort metodi royxat tarkibini o'zgartiradi
# print(mevalar)
# print(mevalar[0])
# mevalar.sort(reverse=True) # sort(reverse=True) bu tartiblab teskari o'girish 
# print(mevalar)

# sorted() bu metodham tartiblaydi faqatgina tarkibini buzmaydi

# yangimevalar = sorted(mevalar)
# print(mevalar[0])
# print(yangimevalar)

# print(sorted(mevalar, reverse=True)) # tartiblab teskari print qilish


# yoshlar = [23, 63, -4, 19, 3,-45, 0, 34, 55, 26]
# yoshlar.sort()
# print(yoshlar)
# print(sorted(yoshlar))
# yoshlar.sort(reverse=True)
# a = sorted(yoshlar, reverse=True)
# print(yoshlar)
# print(a)


# yoshlar.reverse() # royxat qanday bolsa oshani ozini teskari o'giradi
# print(yoshlar)

# len() royxat uzunligi yoki royxat ichida nechta element borligi
# print(len(mevalar))


# range()  --> sonlar ketma ketligini yaratadi

# list() --> boshqa turdan list turiga o'tkazish
# sonlar = list(range(5, 35)) # range() metodi tugash chegarasidan bitta oldingi sonda to'xtaydi
# sonlar = [5,6,7,8,9,10,11,12,13,14]
# print(sonlar)

# sonlar = list(range(11)) # agar boshlangich chegara bo'lmasa unda noldan boshlaydi
# print(sonlar)

# sonlar = list(range(-20, 5))
# print(sonlar)

# sonlar = list(range(5, 21, 2))
# print(sonlar)

# j_sonlar = list(range(2, 30, 2))
# t_sonlar = list(range(1, 30, 2))

# print(j_sonlar)
# print(t_sonlar)


# sonlar = list(range(1, 101, 10))
# print(sonlar[3])

# list, tuple, set, dict

# min(), max(), sum() --> sonli royxatlar uchun
yoshlar = [23, 63, -4, 19, 3,-45, 0, 34, 55, 26]

# print(min(yoshlar)) # sonlar orasidan eng kichigini topib beradi
# print(max(yoshlar)) # sonlar orasidan eng kattasini topib beradi
# print(sum(yoshlar)) # sonlar yigindisi

# hammasini qoshish  sum()
# nechtaligini topish  len()
# bo'lish  /

# ortacha = sum(yoshlar)/len(yoshlar)
# print(ortacha)

# UYGA VAZIFA
# 1. 15 dan -15 gacha bo'lgan sonlar royxatini yarating -> 2 xil usulda
# [15, 14, 13, 12, 11 ........ -13, -14, -15]

# 2. 120-1200 gacha bo'lgan juft sonlar o'rta arifmetigi

# 3. Davlatlar royxati yaratilsin va bir nechta davlat nomi kiritilsin
# shu royxatni sort() va sorted() orqali tartiblansin



