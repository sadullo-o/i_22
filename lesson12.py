# sozlar_en = {
#     'cat': 'mushuk',
#     'dog': 'kuchuk',
#     'car': 'mashina',
#     'apple': 'olma'
# }
# sozlar_uz = {
#     'mushuk': 'cat',
#     'kuchuk': 'dog',
#     'mashina': 'car',
#     'olma': 'apple'
# }

# sozlar = {}
# til = input('1. eng - uz \n2. uz-eng\n>>')
# if til == '1':
#     sozlar = sozlar_en
# elif til == '2': 
#     sozlar = sozlar_uz

# while True:
#     soz = input('Sozni kiriting: ')
#     print(sozlar.get(soz, 'bu soz lugatda mavjud emas'))

#     savol = input('Yana davom etasizmi? (ha/yoq)>> ')
#     if savol == 'yoq':
#         break




# MAVZU
# Funksiyalar
# 1 yaratish jarayoni, 2 ishlatish jarayoni

# def toliq_ism():
#     """Bu funksiya toliq ismni chiqarib beradi"""
#     ism = input('Ismingizni kiriting: ')
#     familiya = input('familiyangizni kiriting: ')
#     print(ism, familiya)


# toliq_ism()

# def toliq_ism(ism, familiya, yosh):
#     """Bu funksiya toliq ismni chiqarib beradi"""
#     print(ism, familiya)



# name = input('Ism kiriting: ')
# surname = input('Faniliya kiriting: ')
# toliq_ism(name, surname, 22)
# toliq_ism(yosh=22, ism='Ali', familiya=surname)

# toliq_ism('Hasan', 'Husanov')

# toliq_ism('Rustam', 'Saidov')

# def yuza(a, b):
#     print(a*b)

# yuza(12, 5)
# yuza(a=12, b=5)

# def toliq_ism(ism, familiya, t_yil=2000):
#     """Bu funksiya toliq ismni chiqarib beradi"""
#     print(ism, familiya, 2023-t_yil)


# toliq_ism('Ali', 'Valiyev', 1996)

# QIYMAT QAYTARUVCHI FUNSKIYA

# def kvadrat(son):
#     kv = son ** 2
#     return kv


# son_kv = kvadrat(4)
# print(son_kv)

# print(kvadrat(3))


# def get_name():
#     ism = input('Ism>> ')
#     return ism

# def get_lastname():
#     familiya = input('Familiya>> ')
#     return familiya


# def toliq_ism():
#     ism = get_name()
#     familiya = get_lastname()
#     return ism + ' ' + familiya

# print("Salom", toliq_ism())



# def avto_info(model, narx, rang, km=0):
#     avto = {
#         'model': model,
#         'narx': narx,
#         'rang': rang,
#         'km': km
#     }

#     return avto


# avto1 = avto_info('Nexia', 10000, 'Oq', 12000)
# avto2 = avto_info('Cobalt', 12000, 'Oq', 24000)
# print(avto1)
# print(avto2)


# sonlar = list(range(1, 51))

# def range_2(min, max, qadam=1):
#     sonlar = []
#     while min <= max: # 1, 6
#         sonlar.append(min)
#         min += qadam
    
#     return sonlar
    
    
    


# sonlar1 = range_2(1, 30)
# print(sonlar1) 




# UYGA VAZIFA
# 1. F dan son so'rab uni juft yoki toqligini chiqarib beruvchi funksiya yarating
# 2. F dan 2 ta son so'rab kattasini aniqlab beruvchi funskiya yarating
# 3. F dan x va y sonlarini sorab x ning y darajasini hisoblab beruvchi funksiya yarating
# 4. Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini
#  tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
# 45 --> 3, 5, 9 
# 20 --> 2, 4, 5, 10
# 5. F dan radius so'rab aylanani radiusi, diametri, uzunligi, yuzi ni lugat qilib qaytarib beradigan
# funksiya yarating
# 6. Berilgan oraliqdan tub sonlarni topib beradigan funksiya, tub son faqat oziga va 1 ga bo'linadigan sonlar 
