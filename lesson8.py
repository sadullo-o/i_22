# if, else, elif
# a = 442
# b = 65

# if a != b:
#     print('aa')
# if a>b:
#     print('a katta')
# elif b > a:
#     print('b katta')
# else:
#     print('ikkalasi teng')

# a == b --> a b ga tengmi
# a > b  --> a b dan kattami
# a < b  --> a b dan kichikmi
# a >= b --> a b dan kattami yoki b ga tengmi
# a <= b --> a b dan kichikmi yoki b ga tengmi
# a != b --> a b ga teng emasmi

# if a > b: print('salom')
# else: print('Xayr')

# bu usulda 2 nuqtalar qo'yilmaydi
# print('salom') if a>b else print('xayr')

# son1 = int(input('Birinchi sonni kiriting: '))
# son2 = int(input('ikkinchi sonni kiriting: '))

# if son1 > son2:
#     print(son1, 'katta')
# elif son2 > son1:
#     print(son2, 'katta')
# elif son2> 45:
#     print('ss')
# elif son1 < 333:
#     print('saaas')
# else:
#     print('Ikkalasi teng')

# and -> va, or -> yoki
# son1 = 15
# son2 = 20
# son3 = 10

# if son1>son2 and son1>son3: # barcha shartlar True bo'lsagina bajariladi
#     print('ss')

# if son1>son2 or son1>son3:  # barcha shartlar orasidan kamida bittasi True bo'lsa bajariladi
#     print('aa') 

# NESTED IF  --> if ichida if
# son = 76

# if son > 40:
#     print('40 dan katta')
#     if son > 60:
#         print('60 dan ham katta')
#     else:
#         print('lekin 60 dan kichik ekan')


# if 4 > 5:
#     pass


# soz = 'nok'

# if soz == 'olma':
#     print('Bu olma')

# royxatlar ichidagi elementni bor yoqligini tekshirish
# cars = {'cobalt', 'nexia', 'damas', 'lacetti'}

# car = input('Mashina kiriting: ')
# # print(car in cars)
# if car in cars:
#     print('Bu mashina bizda bor')
# else:
#     print('Bu mashina bizda yoq')


# matn ichidan matn bor yoqligini tekshirish
# matn = 'Qish fasli juda sovuq bo\'ldi'
# if 'sovuq' in matn:
#     print('Bor ekan')

# royxat yoki string bo'sh yoki bo'sh emasligini tekshirish
# fruits = [23, 53]
# if fruits:
#     print('Bosh emas')
# else:
#     print('Bo\'sh ekan')


# gap = 'sdfdverdsvcsd'
# if gap:
#     print('Gap mavjud')
# else:
#     print('gap yoq')


# yil = int(input('Tugilgan yilingizni kiriting: '))

# yosh = 2023 - yil

# if yosh >= 18:
#     print('Sizga mumkin')
# else:
#     print('Sizga hali mumkin emas')


# yil = int(input('Yilingizni kiriting: '))
# yosh = 2023 - yil

# if yosh < 7 or yosh > 70:
#     print('Sizga bepul')
# elif yosh<18:
#     print('15000 sum')
# elif yosh < 24: 
#     print('20000 sum')
# else:
#     print('25000 sum')


# users = {
#     'ali': 'ali123',
#     'vali': 'vali777',
#     'hasan': 'hasanboy'
# }

# username = input('Username kiriting: ')
# names = users.keys()
# if username in names:
#     parol = input('Parolni kiriting: ')
#     if parol == users[username]:  # 'ali321' --> users['ali'] -->  ali123
#         print('Xush kelibsiz')
#     else:
#         print('Parol xato')

# else:
#     print('Bunday foydalanuvchi yoq')


# UYGA VAZIFA
# 1. cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# shu royxatdagi elementlarni bosh harfini katta qilib 
# print qiling, agar element gm ga teng bo'lsa unda hamma 
# harfini katta qilib print qiling
# 2. son kiritishni sorang, va son noldan kichik bo'lsa manfiy,
# noldan katta bo'lsa musbat, nolga teng bo'lsa nol deb print 
# qilsin


