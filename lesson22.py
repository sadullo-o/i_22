# fayllar bilan ishlash


# FAYLDAN O'QISH
# fayl = open('info.txt')
# matn = fayl.read()
# print(matn)
# fayl.close()


# with open('info.txt') as fayl:
#     matn = fayl.read()
#     print(matn)

# s = ''
# with open('info.txt') as fayl:
#     matn = fayl.readlines()
#     matn = [i.rstrip() for i in matn]
    
#     for i in matn:
#         s += i.title() + '\n'
    
# with open('info.txt', 'w') as fayl:
#     fayl.write(s)
        


# qatorma qator o'qish
# with open('info.txt') as fayl:
#     for i in fayl:
#         print('Salom', i)


# qatorlarni royxatga alohida olish
# with open('info.txt') as fayl:
#     infos = fayl.readlines()
#     infos = [i.rstrip() for i in infos]

# print(infos)



# FAYLGA YOZISH
# 'w'  faylga yozish formati, eski malumotlarni o'chirib o'rniga yozadi, agar fayl mavjud bo'lmasa yangi fayl yaratadi
# 'w+' w ga o'xshaydi, faqat bunda o'qishga ham ruxsat berilgan 
# 'r'  faylni faqat o'qish uchun
# 'r+' faylni o'qish va yozish uchun
# 'a'  faylga malumot yozadi, mavjud malumot ustiga qo'shadi, fayl bo'lmasa yangi yaratadi
# 'a+' a ga o'xshaydi faqat o'qish uchun ham ruxsat bor

# faylnomi = 'matn2.txt'
# with open(faylnomi, 'w') as fayl:
#     d = fayl.read()


# faylnomi = 'matn.txt'
# with open(faylnomi, 'a') as fayl:
#     fayl.write('Rustam\n')


# o'zgaruvchilarni faylga saqlash

# import pickle

# car1 = {
#     'model': 'Nexia',
#     'narx': 9000
# }

# car2 = {
#     'model': 'Cobalt',
#     'narx': 13000
# }


# with open('yangi', 'wb') as fayl:
#     pickle.dump(car1, fayl)
#     pickle.dump(car2, fayl)



# with open('yangi', 'rb') as fayl:
#     car1 = pickle.load(fayl)
#     car2 = pickle.load(fayl)

# print(car1)
# print(car2)




# JSON  --> Javascript Object Notaion, Dasturlash tillari orasida malumot almashuvchi ko'prik
# list, tuple --> Array
# dict --> Object
# int  --> Number
# float --> Number
# True  --> true
# False  --> false
# None  --> null
# ''   -->  ""

# python malumot turini json formatga o'tkazish

# import json

# x = True
# ism = 'Ali'
# json.dumps()  ---> malumotlarni json formatga o'tkazadis
# x_json = json.dumps(x)
# ism_json = json.dumps(ism)
# print(x, x_json)
# print(ism, ism_json)


# json.dump()  --> json formatga o'tkazib faylga saqlaydi

# talaba = {
#     'ism': 'Ali',
#     'familiya': 'Valiyev',
#     'bosqich': 3,
#     'fanlar': [
#         {
#             'nomi': 'Matematika'
#         },
#         {
#             'nomi': 'Fizika'
#         }
#     ]
# }


# with open('talaba.json', 'w') as fayl:
#     json.dump(talaba, fayl)



# jsondan malumotlarni o'qish
# json.loads()  # json formatdan python formatga o'tkazib beradi
# json.load()

# with open('talaba.json') as fayl:
#     r = fayl.read()
#     print(json.loads(r))

# with open('talaba.json') as fayl:
#     talaba = json.load(fayl)

#     print(talaba)






# try except

# son = 5
# print(son+'s')

# son = '5'
# try:
#     print(son + 'ss')
# except:
#     print('Xatolik berdi!!!')

# try:
#     son = '5'
#     print(son+'555')
# except:
#     print('Xatolik berdi')
# else:
#     print('Kod muvaffaqiyatli yakunlandi')


# UYGA VAZIFA
# 1. foydalanuvchidan ism familiya telefon so'rab uni faylga yozib borish  --> 
# doim takrorlanadigan, exit da chiqadigan

# 2. Foydalanuvchidan username, ism, familiya, parol so'rab lugat shakliga keltirib, username --> 
# kalit, ism, familiya, parol qiymat keltirib json faylga qo'shish
# a = {
#     'ali34324': {
#     'ism': 'Ali',
#     'familiya': 'Valiyev'
#     }
# }

# 3. Foydalanuvchidan username va parol so'rab json dagi malumotlarga mos kelsa ism familiya print qilinsin
# aks holda parol yoki username xato deb chiqarsin

