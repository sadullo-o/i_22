# Imtihonni tahlil qilish
# 1
# son1 = int(input('Birinchisini kiriting >> '))
# son2 = int(input('Ikkinchisini kiriting >> '))

# print(f"{son1} va {son2} ni yigindisi {son1+son2} ga teng")
# print(f"{son1} va {son2} ni ayirmasi {son1-son2} ga teng")
# print(f"{son1} va {son2} ni ko'paytmasi {son1*son2} ga teng")
# print(f"{son1} va {son2} ni bo'linmasi {son1/son2} ga teng")

#2 
# ism = 'Ali'
# familiya = 'Valiyev'
# bosqich = 3
# pasport = 'AA4534227'
# info = f"Talaba: \nIsm-familiya: {ism} {familiya} \nBosqich: {bosqich}-kurs \nPasport: {pasport}"
# print(info)

#3
# sonlar = list(range(101, 1000, 2))
# boshi = sonlar[:16]
# summaboshi = sum(boshi)
# oxiri = sonlar[-15:]
# summaoxiri = sum(oxiri)
# ortason = int(len(sonlar)/2)
# ortasi = sonlar[ortason:ortason+16]
# summaortasi = sum(ortasi)

# print(summaboshi, summaortasi, summaoxiri)

#4
# shaxslar = ['Abu Ali Ibn Sino', 'Putin', 'Amir Temur', 'Chingizxon', 'Stiv Jobs', 'Messi', 'Ronaldo', 'Makedonski']
# z_shaxslar = []
# z_shaxslar.append(shaxslar.pop(1))
# z_shaxslar.append(shaxslar.pop(3))
# z_shaxslar.append(shaxslar.pop(3))
# z_shaxslar.append(shaxslar.pop(3))
# print(z_shaxslar)
# print(shaxslar)

#5
# sonlar = (12, 53, 3, 65, 34)
# sonlar = list(sonlar)
# sonlar[2] = 30
# sonlar.sort()
# sonlar = tuple(sonlar)
# print(sonlar)

#6
# qoida lugat (dict) da 2 ta bir xil kalit so'z bo'lishi mumkin emas 
# oquvchilar = {
#     'oquvchi1':{
#         'ism':'Ali',
#         'familiya': 'Valiyev',
#         'sinf': '5-sinf'
#     },
#     'oquvchi2': {
#         'ism': 'Hasan',
#         'familiya':'Husanov',
#         'sinf': '7-sinf'
#     }
# }
# print(oquvchilar['oquvchi2']['familiya'])

#7
# avtosalon = {
#     'nexia':12000,
#     'cobalt': 13000,
#     'jentra': 15000,
#     'damas': 8000,
#     'audi': 30000,
#     'bmw': 34000,
#     'onix': 20000
# }

# car = input('Mashina nomini kiriting: ')
# print(car + ' >> ' + str(avtosalon.get(car.lower(), 'Bu mashina avtosalonimizda mavjud emas')))
