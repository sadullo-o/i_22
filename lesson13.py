# def son(x):
#     if x % 2 == 0:
#         print('Bu son juft')
#     else:
#         print('Bu son toq')


# son(23)


# def son(x, y):
#     print(max(x, y))


# son(22, 25)



# def son(x, y):
#     print(x**y)

# son(5, 2)




# def number(x):
#     ruyxat = list(range(2, 11))
#     for i in ruyxat:
#         if x % i == 0:
#             print(i)


# son = int(input('Son kritilson: '))
# number(son)



# def aylana(r):
#     PI= 3.14
#     ruyxat = {
#         'radius': r,
#         'diametr': 2*r,
#         'uzunlik': 2*PI*r,
#         'yuzi': PI*(r**2)
#     }
#     # ruyxat.append(r)
#     # ruyxat.append(2*r)
#     # ruyxat.append(2*PI*r)
#     # ruyxat.append(PI*(r**2))
#     return ruyxat
# print(aylana(5))



# def tub(min, max):
#     tub_sonlar = []
#     for i in range(min, max+1):
#         tub = True
#         if i == 1:
#             tub = False
#         elif i == 2: 
#             tub = False
#         else:
#             for x in range(2, i):  # 2, 3, 4, 5, 6
#                 if i % x == 0:
#                     tub = False
        
#         if tub:
#             tub_sonlar.append(i)
    
#     return tub_sonlar


# print(tub(1, 20))
# 11 --> 2,3,4,5,6,7,8,9, 10







# MAVZU
# MOSLASHUVCHAN FUNKSIYALAR


#  *args   --> arguments
# def yigindi(*a):
#     yigindi = 0
#     for i in a:
#         yigindi += i
    
#     print(yigindi)


# yigindi(12,43, 56, 1,42,43,23,4564,76,45,87,1)


# def oquvchilar(*ismlar):
#     return list(ismlar)


# oquvchular8B = oquvchilar('Ali', 'Vali', 'Hasan', 'Husan')

# print(oquvchular8B)


# def sonlar(a,b, *c):
#     print(a)
#     print(b)
#     print(c)



# sonlar(12, 4, 21, 453, 213, 54)


# **kwargs  -> keyword arguments

# def avto_info(model, **infos):
#     infos['model'] = model

#     return infos

# print(avto_info('Nexia', rang='Oq', narx=12000, km=12454))


# def lugat_yarat(til ,**lugat):
#     lugat['lang'] = til
#     return lugat


# ozbekcha = lugat_yarat('uz', olma='apple', mushuk='cat', mashina='car')

# print(ozbekcha)


#1. Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
#2. Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
#  Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy 
# ko'rinishda istalgancha berilishi mumkin bo'lsin.


# def kopaytma(*sonlar):
#     natija = 1
#     for i in sonlar:
#         natija *= i
    
#     return natija


# print(kopaytma(12, 3, 2, 4,5))

# def lugatt(ism_familiya ,**lugat):
#     lugat['F.I.O']=ism_familiya
#     return lugat

# talaba = lugatt('Sardor Alimov', yoshi=19, viloyati='Andijon', tel='+998999093757')

# print(talaba)








# import modullar

# print(modullar.kopaytma(12, 42,13,4))

# print(modullar.PI)

# from modullar import PI, PAROL, kopaytma

# print(PI)
# print(PAROL)


# from modullar import *  # modullarni ichidan barcha narslarni chaqirib olish

# print(PI)
# print(PAROL)
# print(kopaytma(12,42,12))


# chqirilgan narsalarga qisqa nom berish

# import modullar as m

# print(m.PI)


# from modullar import PAROL as pl, PI as p

# print(pl)
# print(p)



# RANDOM
# import random as r
# from random import randint

# son1 = r.randint(10, 20)  # oraliqdan taxminiy bitta sonni chiqarib beradi
# print(son1)


# mevalar = ['olma', 'anor', 'nok', 'behi', 'banan', 'ananas']

# taxminiy_meva = r.choice(mevalar)  # royxat ichidan taxminiy bittasini olib beradi

# print(taxminiy_meva)



# mevalar = ['olma', 'anor', 'nok', 'behi', 'banan', 'ananas']

# r.shuffle(mevalar)

# print(mevalar)



# UYGA VAZIFA
# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar 
# ro'yxatni qaytaruvchi funksiya yozing.  Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning 
# yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish
#  had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# n = 55

