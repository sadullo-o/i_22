# Python OOP --> Obyektga yo'naltirilgan dasturlash sifatida
# Obyekt xususiyati
# Obyekt metodi

# car obyekti --> xususiyati (rangi, narxi, modeli, turi), metodlari (gaz(), tormozlash(), signal(), start())

# Class --> obyekt yaratish uchun qolip (shablon)


# ism = 'Ali'  --> str clasiga tegishli --> String
# x = 67

# print(type(x))


# CLASS lar uchun metodlar 2 xil bo'ladi. Oddiy metodlar va dunder metodlar __metodnomi__
# class Talaba:
#     """Bu klas talaba yaratish uchun qolip"""
#     def __init__(self, ism, familiya, tyil):
#         self.name = ism
#         self.lastname = familiya
#         self.bday = tyil
    
#     def tanishtir(self):
#         return f"Talaba: {self.name} {self.lastname}. Tugilgan yili: {self.bday}"

#     # getter lar
#     def get_name(self):
#         return self.name

#     def get_lastname(self):
#         return self.lastname

#     def get_bday(self):
#         return self.bday    

#     def get_age(self, hyil=2023):
#         return hyil - self.bday    
    
#     def get_bosqich(self):
#         pass
#     def get_diplom(self):
#         pass

# talaba1 = Talaba('Ali', "Valiyev", 1999)  # Talaba clasiga tegishli --> Talaba malumot turi

# talaba2 = Talaba('Hasan', 'Husanov', 2000)

# print(talaba1.lastname)
# print(talaba2.lastname)


# print(talaba1.tanishtir())


# print(talaba1.get_lastname())

# print(talaba2.get_age(2034))



# Amaliy mashq
# User klasi yaratilsin --> ism, username, email, parol
# Bu klas uchun info metodi yaratilsin va bu metodda malumotlar chiroyli tarzda print qilinsin
# Har bir xususiyat uchun getter yaratilsin
# Klasdan bir nechta obyekt olinib tekshirib ko'rilsin




# OBYEKTLAR BILAN ISHLASH

class Talaba:
    """Bu klas talaba yaratish uchun qolip"""
    def __init__(self, ism, familiya, tyil, bosqich):
        self.name = ism
        self.lastname = familiya
        self.bday = tyil
        self.bosqich = bosqich
    
    def tanishtir(self):
        return f"Talaba: {self.name} {self.lastname}. Tugilgan yili: {self.bday}"

    # getter lar
    def get_name(self):
        return self.name

    def get_lastname(self):
        return self.lastname

    def get_bday(self):
        return self.bday    

    def get_age(self, hyil=2023):
        return hyil - self.bday    
    
    def get_bosqich(self):
        return self.bosqich
    def get_diplom(self):
        pass

    # setter lar
    def set_bosqich(self, bosqich):
        self.bosqich = bosqich

    def update_bosqich(self):
        self.bosqich += 1

talaba1 = Talaba('Ali', "Valiyev", 1999, 2)
talaba2 = Talaba('Hasan', "Husanov", 1997, 4)
talaba3 = Talaba('Ravshan', "Rustamov", 2001, 1)
talaba4 = 'ssss'
# talaba1.set_bosqich(5)

# talaba1.update_bosqich()
# print(talaba1.get_bosqich())



class Fan:
    def __init__(self, nomi):
        self.nom = nomi
        self.talabalar = []
        self.talabalar_soni = 0
    
    def add_student(self, *talaba):
        for i in talaba:
            self.talabalar.append(i)
            self.talabalar_soni += 1
        # self.talabalar.append(talaba)
        # self.talabalar_soni += 1
    
    def get_talabalar(self):
        return [talaba.tanishtir() for talaba in self.talabalar]



fan1 = Fan('Matematika')

fan1.add_student(talaba1, talaba2, talaba3)
# fan1.add_student(talaba2)
# fan1.add_student(talaba3)


# print(fan1.get_talabalar())

print(fan1.talabalar_soni)

# print(dir(Talaba))

# Obyekt xususiyatlarini lugat ko'rinishida chiqarib beradi
# s = talaba1.__dict__
# print(s)


#UYGA VAZIFA
# Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar 
# (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering 
# (masalan, kilometer=0)

# Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing

# get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin

# Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.

# update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin

# Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, 
# manzili, sotuvdagi avtomobillar va hokazo)

# Avtosalonga yangi avtomobillar qo'shish uchun metod yozing

# Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing

# Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring



        
