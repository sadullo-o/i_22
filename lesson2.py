# UYGA VAZIFA
# viloyat = 'Buxoro'
# shahar = 'Buxoro'
# mahalla = 'Rabotiqalmoq'
# uy = '129'
# manzil = viloyat + ' viloyati ' + shahar + ' shahri ' + mahalla + ' mahallasi ' \
#     + uy + ' -uy'
# manzil2 = f'{viloyat} viloyati {shahar} shahri {mahalla} mahallasi {uy} -uy'
# print(manzil)
# print(manzil2)


# Sonlar  --> Integer va Float
# Integers (int) --> bu oddiy butun sonlar (manfit, nol, musbat)
# son1 = 15
# son2 = -8
# son3 = 0

# t_1 = 15
# t_2 = 10
# s = t_1 * t_2


# Float (float) --> bu o'nli sonlar

# son1 = 5.4
# son2 = 19.8
# son3 = -4.6

# x = son1 * son3
# print(x)
# Qoida: float sonlar qatnashgan amallar natijasi float bo'ladi
# s1 = 4.6
# s2 = 3.4
# print(s1+s2)

# aholi = 7_549_000_000
# print(aholi+1)

# Konstanta
# PI = 3.14
# KALIT = 's7gv3u8s'


# x = 12
# y = 'salom'
# z = 5.4
# 
# x,y,z = 12, 'salom', 5.4
# print(y)


# Casting --> bu bir malumot turidan boshqa malumot turiga o'girish

# str() --> boshqa malumot turidan String malumot turiga o'girish
# int()  --> boshqa malumot turidan Integer malumot turiga o'girish
# float() --> boshqa malumot turidan Float malumot turiga o'girish

# yosh = 23 
# print('Mening yoshim '+ str(yosh))

# yil = '2023'
# print(int(yil) - 1999)

# print(float(45))

# x = 12
# y = 'salom'
# z = 5.4
# type()  malumot turini chiqarib beradi
# print(type(x))
# print(type(y))
# print(type(z))

# Input  --> console da yozish uchun joy yaratib beradi

# input('Ismingizni kiriting: ')

# ism = input('Ismingizni kiriting: ')
# print('Salom', ism)
# Qoida --> input doim matn qaytaradi

# son = int(input('Son kiriting: '))
# print(son,' ni kubi--> ',son**3)

# print(int(son)**2)

# Amaliy mashq: Foydalanuvchidan tugilgan yilini so'rab uni yoshini hisoblab
# beradigan kod yozing
# t_yil = int(input('Tugilgan yilingiz: '))
# print(2023-t_yil)



# Ro'yxatlar --> list

sonlar = [12,43,42,18, 86]
sozlar = ['olma', 'shahar', 'dunyo', 'respublika', 'dunyo']
aralash = [12, 5.6, -42, 'O\'zbekiston', "Toshkent chiroyli shahar"]
bosh = []
# royxat elementlari indekslari noldan boshlanadi

# print(type(bosh))
# print(aralash[3], sozlar[3].capitalize()+'si')
# print(aralash[4].title())
# print(sonlar[-1])

# matn = 'olma shirin meva'
# print(matn.title())

# royxatga yangi element qo'shish

# royxatni oxiridan yangi element qo'shish uchun
# sonlar.append(234)
# bosh.append('Samarqand')
# bosh.append('Buxoro')
# bosh.append('Xiva')
# print(bosh)
# print(bosh[0])

# insert()  --> indeks bo'yicha yangi element qo'shish
# sozlar.insert(2, 'qizil')
# print(sozlar)


# royxat elementini o'zgartirish
# aralash[2] = 10
# print(aralash)


# royxat elementini o'chirish

# del -> indeks bo'yicha o'chirish
# del aralash[2]
# print(aralash)

# a = 34
# del a

# remove(qiymat)  --> royxat tarkibidan birinchi duch kelgan qiymatni o'chiradi
# sozlar.remove('dunyo')
# print(sozlar)


# pop() royxatdan elementni sugurib olish
# son = sonlar.pop(1)
# print(sonlar)
# print(son)

# son = sonlar.pop()  # oxirgi elementni sugirib oladi
# print(son)



# UYGA VAZIFA
# 1. ismlar royxati yaratilsin va kamida 4 ta ism qo'shilsin -->
#  har bir ism uchun print orqali xabar chiqarilsin

# 2. sonlar royxati yaratilsin va musbat manfiy o'nli sonlar kiritilsin
# Va sonlar ustida amallar bajarilib print qilinsin

# 3. mehmonlar degan royxat yaratilsin va 5 ta taklif qilingan mehmon ismi
# kiritilsin.
# --> kelganlar royxati yaratilib mehmonlar dan kelganlarini sugurib joylashtirish

# 4. shaharlar royxati yartilsin bir nechta shahar kiritilsin; Va shu royxatni boshiga
# oxiriga va orasiga yangi elementlar qo'shilsin
