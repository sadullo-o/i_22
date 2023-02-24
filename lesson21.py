# dunder metodlar  --> oldindan yaratilgan metodlar bo'lib, qandaydir vazifalarga yo'naltirilgan
# __nom__  
# double underscore  -> dunder

class Avto:
    def __init__(self, model, rang, narx, km):
        self.model = model
        self.narx = narx
        self.rang = rang
        self.km = km
        self.marafet = ['Tonirovka', 'Balon', 'Lyuk']
    
    def __repr__(self):  # print() qilish uchun xizmat qiladi
        return 'Avtomobil: '+ self.model  # qachonki Avto klasidan yaratilgan obyektni (avto1, avto2, avto3,...) print() qilgan qanday natija chiqarishini belgilaydi

    # 2 ta avto obyektlarini taqqoslash uchun dunder metodlari
    # __lt__   --  <
    # __le__   --  <=
    # __gt__   --  >
    # __ge__   --  >=
    # __eq__   --  ==
    # __ne__   --  !=
    def __gt__(self, boshqa):
        return self.narx > boshqa.narx

    def __lt__(self, boshqa):
        return self.narx < boshqa.narx
    
    def __eq__(self, boshqa):
        if self.narx == boshqa.narx:
            m = 'Teng ekan'
        else:
            m = 'Xato ekan'
        return m
    
    def __len__(self):
        return self.km
    
    def __getitem__(self, index):
        return self.marafet[index]
    
    def __setitem__(self, index, qiymat):
        self.marafet[index] = qiymat
        print(self.marafet)


    # +    __add__
    # -    __sub__
    # *    __mul__
    # /    __div__
    # **   __pow__
    def __add__(self, nimadir):
        self.marafet.append(nimadir)
        print(self.marafet)

    
    # def __call__(self):
    #     print(self.model + ' ' + str(self.narx) + ' ' + self.rang)
    # def __call__(self, nimadir):
        # print(nimadir, self.model + ' ' + str(self.narx) + ' ' + self.rang)
    def __call__(self, *nimadir):
        for i in nimadir:
            print(i, self.model)
    

    
    

    


avto1 = Avto('Nexia', 'Oq', 9000, 35000)
avto2 = Avto('Cobalt', 'Oq', 19000, 14000)

# print(avto1)
# print(avto2)
        

# print(avto1==avto2)


# print(len(avto2))

# s = [4,2,4,6,7,34]
# print(s[2])

# print(avto1[0])

# avto1[2] = 'Gazbalon'


# avto1 + 'Motor'
# avto1 + 'Gazbalon'

# print(avto1())
# avto1()

# avto1('Malumot: ')

# avto1('Avto', 'Car', 'Mashina')


# Amaliy mashgulot
# Avtosalon klasi yaratilsin, va mashinalar royxati qoshilsin
# avtosalon1 + 'Nexia'  --> mashinalar royxatiga Nexia qo'shilsin

# class Avtosalon:
#     def __init__(self, nom):
#         self.nom = nom
#         self.avtolar = []

#     def __add__(self, mashina):
#         self.avtolar.append(mashina)
        

# avtosalon1 = Avtosalon('Uzavto')

# avtosalon1 + 'Nexia'
# avtosalon1 + 'Cobalt'

# print(avtosalon1.avtolar)


# UYGA VAZIFA
# Talaba klasi yaratilsin, xususiyatlar berilsin
# Shu klas obyektlari uchun  --> print(), talaba1>talaba2 --> kurs bo'yicha taqqoslasin

# Fan klasi yaratilsin nomi, talabalari = [] qo'shilsim
# fan1 + talaba2 --> talabalari ga talaba2 append qilinsin
# print(fan1)  --> ichidagi talabalar ismlari chiqsin