# UYGA VAZIFA
# 1. 

# with open('matn.txt', 'a') as fayl:
#     while True:
#         ism = input('ISM>> ')
#         parol = input('PAROL>> ')
#         m = ism + ', ' + parol + '\n'
#         fayl.write(m)

#         savol = input('Chiqish uchun exit ')
#         if savol == 'exit':
#             break


import json
# with open('tabala.json', 'a') as fayl:
#     talabalar = []
#     while True:
#         username = input('Username>> ')
#         ism = input('ISM>> ')
#         parol = input('PAROL>> ')

#         m = {
#             username: {
#             'ism': ism,
#             'parol': parol
#             }
#         }
#         talabalar.append(m)
#         savol = input('Chiqish uchun exit ')
#         if savol == 'exit':
#             break

#     json.dump(talabalar, fayl)
# username = input('username>> ')
# parol = input('parol>> ')

# with open('tabala.json') as fayl:
#     a = json.load(fayl)
#     for i in a:
#         if username in i.keys():
#             if parol == i[username]['parol']:
#                 print(i[username]['ism'])
    


# Xatolar bilan ishlash

# print('ss' + 4)
# a = [3]

# print(a[4])

# try except
# yosh = input('Tugilgan yilingiz>> ')

# try:
#     yosh = int(yosh)
#     print(2023-yosh)
# except:
#     print('Siz xato yil kiritdingiz')
# else:
#     print('Kod muvaffaqiyatli yakunlandi!!')

# else qismi qachonki try ishlasha ishlaydi


# ZeroDivisionError

# try:
#     print(3+'ss')
# except ZeroDivisionError:
#     print('0 gan bolish mumkin emas')


# IndexError
# mevalar = ['olma', 'anor', 'behi']

# try:
#     print(mevalar[4])
# except IndexError:
#     print(f"Kechirasiz bizda faqat {len(mevalar)} ta meva bor")



# Key error --> lugatda mavjud bo'lmagan kalit soz chaqirilsa


# FileNotFoundError -->  faylni o'qishda xato nom kiritilsa



# mevalar = ['olma', 'anor', 'behi']

# try:
#     print(mevalar[1])
#     print(5/0)
# except IndexError:
#     print(f"Kechirasiz bizda faqat {len(mevalar)} ta meva bor")
# except ZeroDivisionError:
#     print('Nolga bolish mumkin emas')
# else:
#     print('Kod yakunlandi')


# Amaliy mashgulot
# Foydalanuvchidan son so'rab kvadratini chiqaradigan dastur, while da
# Foydalanuvchi sonni orniga matn kiritsa ham kod xatolik bermasdan ishlasin


# while True:
#     son = input('Son kiriting>> ')
#     try:
#         print(int(son)**2)
#     except:
#         print('Notogri formatdagi son kiritdingiz, qayta kiritib koring')
#     else:
#         savol = input('Davom etasizmi>> ')
#         if savol == 'yoq':
#             break




# Ichki kutubxonalar  (modullar)
# datetime  -> sana, vaqt (kun oy yil soat minut sekund)

import datetime as dt

hozir = dt.datetime.now()  #hozirgi sana va vaqtni oladi

# print(hozir)

# kun = hozir.date()  # sanani oladi
# print(kun)

# vaqt = hozir.time() # vaqtni oladi
# print(vaqt)

# soat = hozir.hour
# daqiqa = hozir.minute
# sekund = hozir.second

# print(soat)
# print(daqiqa)
# print(sekund)



#
# bugun = dt.date.today()  # faqat sanani oladi
# ramazon = dt.date(2023, 3, 23) 

# farq = ramazon-bugun

# print(f"Ramazongacha {farq.days} kun qoldi")

# date dan faqat date ni ayrib bo'ladi, datetime faqat datetimeni ayrib bo'ladi


# hozir = dt.datetime.now()
# futbol = dt.datetime(2023, 2, 14, 11, 15, 0)

# farq = futbol - hozir
# sekundlar = farq.seconds
# daqiqa = sekundlar / 60
# soat = daqiqa / 60

# print(soat)


# hozir = dt.datetime.now()
# s = hozir.strftime("%H:%M")
# print(s)

# s = hozir.strftime('%d/%m/%Y')
# print(s)

# s = hozir.strftime("%d-%m-%Y, %H:%M")
# print(s)




# math
import math

# pisoni = math.pi
# print(pisoni)


# print(math.sin(1))

# print(math.log(9))
# print(math.log10(100))


son = 5.9

# print(math.ceil(son)) # tepaga qarab yaxlitlaydi
# print(math.floor(son)) # pastga qarab yaxlitlaydi

# print(math.sqrt(16)) # ildiz

# print(math.pow(3, 4))  # daraja



# pprint --> printni chiroyli versiyasi

from pprint import pprint
# a = [{"ali55": {"ism": "ALi", "parol": "Valiyev"}}, {"hasan7788\\": {"ism": "Hasan", "parol": "Husanov"}}]

# b = {
#     "ali55": {
#         "ism": "ALi", 
#         "parol": "Valiyev"
#         }
#     }

# print(b)

# pprint(b)
# import json
# with open('tabala.json') as fayl: 
#     a = json.load(fayl)

# print(a)

# pprint(a)





# RegEx  -> andoza

import re

# sozlar = ['anor', 'behi', 'shahar', 'shior', 'bemor']

# andoza = "^s....r"

maillar = ['ali@mail.ru', 'vali@gmailru', 'hasangmail.com', 'husan@gmail.com']
emailandoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'

# for i in maillar:
#     if re.match(emailandoza, i):
#         print(i)

# email = input('Mail pochta>> ')
# if re.match(emailandoza, email):
#     print('Qabul qilindi')
# else:
#     print('Xato mail kiritdingiz')


# telandoza = '^[\+]?[(]?[8-9]{3}[)]?[-\s\.]?[0-9]{2}[-\s\.]?[0-9]{7}$'

# tel = '+998934433554'

# if re.match(telandoza, tel):
#     print('Togri')
# else:
#     print('Xato')



# telandoza = '^[\+]?[(]?[8-9]{3}[)]?[-\s\.]?[0-9]{2}[-\s\.]?[0-9]{7}'
# mailandoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'

# matn = '''+998919263599 ali@mail.ru sssac   sachasbj ashbx jgas vali@gmail.com sdasdc'''

# phones = re.findall(telandoza, matn)
# print(phones)



# UYGA VAZIFA
# matn ichidan website manzillarini ajratib oladigan andoza yarating
# https://kun.uz

# https://ihateregex.io/  --> andoza yaratib beruvchi sayt