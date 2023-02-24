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



# Dictionary (dict) --> Lugat 
# olma -- apple
# mashina -- car
# mushuk -- cat


# lugat = {
#  kalitsoz : qiymat,
# }

# mashina = {
#     'model': 'Cobalt',
#     'rang': 'oq',
#     'narx': 12000,
#     'km': '10 km',
#     'xususiyatlari': ['yaxshi', 'ozgina muammo bor', 'yengilgina', 'qimmat']   
# }

# mashina2 = {}  # bo'sh figurali qavs kelsa bu dict 

# baholar = {
#     'Ali': 5,
#     'Vali' : 3,
#     'Hasan': 4
# }

# talaba1 = dict(ism='hasan', familiya='Husanov', bosqich=3)

# print(baholar)

# print(talaba1)


# Lugatlar ham tartiblanmagan yani element indekslari mavjud emas
# lugat elementlarini ishlatish
# 1-usul
# print(baholar['Ali'])
# print(mashina['rang'])


# print(mashina['raqam'])
# get() --> kalitso'z bo'lsa qiymatini oladi bo'lmasa xabarni chiqaradi
# print(mashina.get('narx', 'Bunday qiymat mavjud emas'))



# keys() --> lugat kalitso'zlarini oladi
# values() --> lugat qiymatlarini oladi
# items()  --> lugatning kalit-qiymat juftliklarini oladi

# kalitlar = mashina.keys()
# print(kalitlar)

# qiymatlar = mashina.values()
# print(qiymatlar)

# juftliklar = mashina.items()
# print(juftliklar)




# mashina = {
#     'model': 'Cobalt',
#     'rang': 'oq',
#     'narx': 12000,
#     'km': '10 km',
#     'xususiyatlari': ['yaxshi', 'ozgina muammo bor', 'yengilgina', 'qimmat']   
# }

# qiymatlarni o'zgartirish
# mashina['narx'] = 13000
# mashina['rang'] = 'qora'
# print(mashina)

# update()
# mashina.update({'km':'100 km', 'rang':'seriy'})
# print(mashina)

# yangi element qo'shish
# mashina['yil'] = 2022
# print(mashina)

# update()
# mashina.update({'raqam':'80 T 872 PA'})
# print(mashina)


# lugatdan qiymatni o'chirish

# del mashina['km']
# print(mashina)

# a = mashina.pop('rang')
# print(a)
# print(mashina)

# lugatni oxirgi elementini o'chiradi
# mashina.popitem()
# print(mashina)


# clear()  bu lugatni tozalaydi
# mashina.clear()
# print(mashina)


# lugatdan nusxa olish
# mashina = {
#     'model': 'Cobalt',
#     'rang': 'oq',
#     'narx': 12000,
#     'km': '10 km',
#     'xususiyatlari': ['yaxshi', 'ozgina muammo bor', 'yengilgina', 'qimmat']   
# }

# mycar = mashina.copy()
# print(mycar)

# mycar = dict(mashina)
# print(mycar)



# NESTED Lugat--> lugat ichida lugat
# talabalar = {
#     'talaba1': {
#         'ism':'Ali',
#         'familiya':'Valiyev',
#         'bosqich': 4
#     },
#     'talaba2': {
#         'ism':'Hasan',
#         'familiya':'Husanov',
#         'bosqich': 3
#     }
# } 

# print(talabalar['talaba2']['familiya'])

# print(talabalar['talaba1']['bosqich'])


# UYGA VAZIFA
# 1. ingliz-o'zbek lugatini python lugat sifatida yarating: 10 ta so'z
# 'cat':'mushuk', 
# foydalanuvchidan so'z so'rang va tarjimasini chiqarib bering,
# agar so'z lugatimizda mavjud bo'lmasa foydalanuvchiga xabar berib qo'ying

# 2. davlatlar va ularning poytaxti lugatini yarating: kamida 5 ta davlat
# foydalanuvchidan davlat nominib so'rab unga mos poytaxtni chiqarib
# beradigan kod yozing