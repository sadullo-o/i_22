# UYGA VAZIFA
# 1
# 2
# 22, 2*10+2
# 222, 22*10+2
# 2222, 222*10+2
# 22222, 2222*10+2

# n=3   #2+22+222
# start = 2
# yigindi = 0

# for i in range(0, n):
#     yigindi += start
#     start = start * 10 + 2  # 2222

# print(yigindi)


# 2
# raqam = int(input("Son kritilsin"))
# k = '*'
# for i in range(1, (raqam) + 1):
#     for j in range(0, i):
#         print(k, end='')
#     print()
# for i in range(1, (raqam) + 1):
#     for j in range(0, raqam-i):
#         print(k, end='')
#     print()


# while --> takrorlanuvchi operator, shart orqali chegara beriladi
# son = 1
# while son <= 5:  # toki son 5 dan kichik ekan kod bajarilsin
#     print(son)
#     son += 1



# savol = ''
# while savol != 'chiqish':
#     savol = input('Ismingizni kiriting, agar dasturdan chiqmoqchi bolsangiz "chiqish" deb yozing: ')
#     print(savol)


# ishora usuli (flag)
# ishora = True
# while ishora:
#     gap = input('Ismingizni kiriting, chiqish uchun "exit": ')
#     if gap != 'exit':
#         print(gap)
#     else:
#         ishora = False


# break operatori
# while True:
#      gap = input('Ismingizni kiriting, chiqish uchun "exit": ')
#      if gap != 'exit':
#         print(gap)
#      else: # agar exit ga teng bo'lsa
#         break


# continue --> qaysi qadamga kelib continue berilsa o'sha qadam tashlab ketiladi
# son = 0
# while son <= 10:
#     son += 1
#     if son % 5 == 0:
#         continue
#     else:
#         print(son)


talabalar = []
while True:
    bolim = input('''Quyidagi bo'limlardan birini tanlang:
    1. Info
    2. Qabul
    3. Talabani chetlashtirish
    4. Talabalarimiz
    0. Chiqish \n>>''')

    if bolim == '1':
        print('Biz Inha universitetimiz. Bizda .... fakultetlari mavjud')
    elif bolim == '2':
        ism = input('Ismingizni kiriting: ')
        talabalar.append(ism)
        print('Talaba qabul qilindi')
        print()
    elif bolim == '3':
        ism = input('Talaba ismi>>')
        if ism in talabalar:
            talabalar.remove(ism)
        else:
            print('Bizda bunday talaba oqimaydi')

    elif bolim == '4':
        t = ''
        for i in talabalar:
            t += i + '\n'
        print(t)
    elif bolim == '0':
        break
    else:
        print('Bizda bunday bolim mavjud emas')



# UYGA VAZIFA
# LUGAT Dasturi
# foydalanuvchi so'z kiritsin va u soz 
# tarjimasi bizni lugatimizda bo'lsa tajrima qilib bersin
# aks holda bu so'z bizda mavjud emas deb xabar bersin
# doimiy takrorlanadigan dastur, agar exit deb yozsa dastur tugasin
