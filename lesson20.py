# Vorislik va polimorfizm

# Vorislik  
# super klass
# class Shaxs:
#     def __init__(self, ism, familiya, tyil):
#         self.name = ism
#         self.lastname = familiya
#         self.bday = tyil

#     def get_info(self):
#         return self.name + ' ' + self.lastname
    
#     def get_age(self):
#         return 2023-self.bday
    

# # shaxs1 = Shaxs('Ali', 'Valiyev', 1998)
# # print(shaxs1.get_info())
# # print(shaxs1.get_age())
        
# # voris klass
# class Talaba(Shaxs):
#     def __init__(self, ism, familiya, tyil, bosqich, fakultet):
#         super().__init__(ism, familiya, tyil)
#         self.bosqich = bosqich
#         self.fakultet = fakultet
    
#     # polimorfizm
#     def get_info(self):
#         return super().get_info()+ ' ' + self.fakultet
    
#     def get_bosqich(self):
#         return self.bosqich
    
#     def get_fakultet(self):
#         return self.fakultet



# talaba1 = Talaba('Ali', 'Valiyev', 2000, 4, 'Tarix')
# shaxs1 = Shaxs('hasan', 'Husanov', 1977)

# print(talaba1.get_info())
# print(talaba1.get_age())
# print(talaba1.get_fakultet())
        

# Polimorfizm --> super klasda yaratilgan metodlarni voris klasda qayta yozish





from uuid import uuid4
# Inkapsulyatsiya  --> kapsulaga olish -> himoya qilish
class Avto:
    avtolar_soni = 0
    def __init__(self, model, narx, rang, yil, km=0):
        self.model = model
        self.narx = narx
        self.rang = rang
        self.yil = yil
        self.__km = km
        self.__id = uuid4()
        Avto.avtolar_soni += 1


    def get_km(self):
        return self.__km
    
    def add_km(self, km):
        if km>0:
            self.__km += km
        else:
            print('Km ni kamaytirish mumkin emas')
    
    def get_id(self):
        return self.__id
    

    # classning shaxsiy metodi
    @classmethod
    def get_avtolar_soni(cls):  # class
        return cls.avtolar_soni



avto1 = Avto('Gentra', 15000, 'oq', 2022, 5000)
avto2 = Avto('Cobalt', 12000, 'qora', 2022, 10000)

avto3 = Avto('Gentra', 15000, 'oq', 2022, 5000)
avto4 = Avto('Cobalt', 12000, 'qora', 2022, 10000)
# print(avto1.__id)
# print(avto2.__id)

# print(avto2.__km)

# avto2.add_km(12000)

# print(avto1.get_id())
# print(avto2.get_km())


print(Avto.get_avtolar_soni())



# AMALIY MASHQ
# Xodim clasi yaratilsin, xususiyatlar, metodlar yaratilsin
# Direktor klasiu yaratilib Xodim klasidan voris qilib olinsin
# Direktor klasiga metodlar yozilsin


# super klass, ota klass
# class Xodim:
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
    
#     def get_info(self):
#         return self.ism + ' ' + self.familiya
    
# # Voris klass
# class Direktor(Xodim):
#     def __init__(self, ism, familiya, tyil, lavozim):
#         super().__init__(ism, familiya, tyil)
#         self.lavozim = lavozim
    
#     def get_info(self):
#         return self.lavozim
        
    
# direktor = Direktor('Ali', 'Valiyev', 1979, 'Korxona direktori')

# print(direktor.get_info())


# UYGA VAZIFA
# Transport klasi yaratilib xususiyatlar va metodlar qo'shilsin
# Avtomobil klasi yaratilib Transportdan voris olinsin va yangi xususiyat metodlar qo'shilsin
# Poyezd klasi yaratilib Transport klasidan voris olinsin
# Avtomobil va Poyezd uchun get_info() metodi qayta moslashtirib yozilsin
# Transport, Avtomobil, Poyezd klasi uchun shaxsiy transportlar_soni xususiyati va shu uchun get metodi yaratilsin
# obyektlar yaratilib ishlatib ko'rilsin