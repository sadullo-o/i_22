#print('Salom Ali')
#print(45)
#print(19+6)

# +  qo'shish
# -  ayrish
# *  ko'paytirish
# /  bo'lish
# // bolish va butun qismini olish
# ** daraja
# %  qoldiq qismi

# print(5 + 3)
# print(10-4)
# print(4*12)
# print(24/4)
# print(15//4)
# print(12//2)
# print(3**4)
# print(25**0.5)
# print(21%4)

# CTRL  C  --> kopirovat 
# CTRL  V  --> vstavit



# O'zgaruvchilar
# ism = 'Hasan'  # o'zgaruvchi bu --> ism,  'Ali' esa o'zgaruvchi qiymati
# familiya = 'Husanov'
# yosh = 29

# print(ism, yosh, 'Husanov', 'Talaba', 'Buxoro')
# print(yosh)
# qoida --> matnga matnni va songa sonni qo'shish mumkin
# print(ism + yosh)
# print(ism + ' ' + familiya)

# Matnlar bilan ishlash  --> String (str)
#  'matn', "matn", '''matn''', """matn""", f''

# shahar = 'Toshkent chiroyli shahar'
# davlat = "Angliya katta davlat"
# davlat_2 = "O'zbekiston"
# gap = '''Men O\'zbekistonda yashayman.
# Davlatim chiroyli'''
# gap = 'Men O\'zbekistonda yashayman. \nDavlatim chiroyli'


# print(gap)


# ism = 'Ali'
# familiya = 'Valiyev'
# yosh = 25
# malumot = 'Mening ismim ' + ism + 'Yoshim '+ yosh  --> xato
# f string ichida ochilgan joyga faqat 1 ta o'zgaruvchi qo'yib bo'ladi
# lekin bir nechta son ustida amal bajarsa bo'ladi
# malumot = f'Mening ismim {ism} {familiya}. Yoshim: {yosh+10} da'
# print(malumot)


# String metodlari
# Metodlar bu qandaydir vazifa bajaradigan funksiyalar

# ism = 'Ali'
# familiya = 'Valiyev'
# upper() metodi barcha harflarni katta qilib beradi
# print(ism.upper(), familiya.upper())


# ism = 'ALI'
# familiya = 'VAliYev'
# lower() metodi barcha harflarni kichraytirib beradi
# print(ism.lower(), familiya.lower())

# matn = 'olma shirin meva'
# title metodi har bir so'zni bosh harfini kattalashtirib beradi
# print(matn.title())

# matn = 'olma shirin meva'
# capitalize  metodi faqatgina birinchi sozni bosh harfini kattalashtirib beradi
# print(matn.capitalize())

# strip(), lstrip(), rstrip()  bular ikki tomondan, chap tomondan, o'ng tomondan bo'shliqlarni olib tashlaydi

# meva = '    olma   '

# print(meva.strip()+' shirin')
# print(meva.lstrip()+' shirin')
# print(meva.rstrip()+' shirin')


# UYGA VAZIFA
# viloyat, shahar, mahalla, uy  o'zgaruvchilari yaratilsin va unga qiymat
# berilsin. Hammasini birlashtirib manzil o'zgaruvchisi yaratilsin va print qilinsin.
# misol uchun: ... viloyati ... shahri ..... mahallasi .....-uy
# shu narsani f string va oddiy string usulida qilinsin
