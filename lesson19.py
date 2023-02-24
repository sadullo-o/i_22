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


class Avto:
    def __init__(self,model,rang,korobka,narx,kilometer,pozitsiyasi ):
        self.model=model
        self.color=rang
        self.korobka=korobka
        self.price=narx
        self.km=kilometer
        self.pozitsiya=pozitsiyasi
        
    def jami(self):
        return f"Avtomobil haqida ma'lumotlar \nModel: {self.model} \nRangi: {self.color} \nUzatish qutisi: {self.korobka} \nNarxi: {self.price} \nProbegi: {self.km}"

    def get_model(self):
        return self.model
    def get_color(self):
        return self.color
    def get_korobka(self):
        return self.korobka
    def get_price(self):
        return self.price
    def get_km(self):
        return self.km
    def get_poz(self):
        return self.pozitsiya
    
    # # update km
    def update_km(self, km):
        if km>0:
            self.km += km
        else: 
            print('Km ni orqaga qaytarish mumkin emas!!!')

# avto=Avto("Gentra","oq","Avtomat","140 000 000 so`m",1,3)

# print(avto.korobka)

# avto.update_km(-1500)

# avto.pozitsiya=4

# print(avto.km)



class Avtosalon:
    def __init__(self, nomi, manzili):
        self.nom = nomi
        self.manzil = manzili
        self.cars = []
        self.cars_num = 0

    
    def add_car(self, *avto):
        for i in avto:
            self.cars.append(i)
            self.cars_num += 1
    
    def salon_cars(self):
        return [car.model + ' ' + car.price for car in self.cars]  # ['Gentra', 'Cobalt', 'Malibu']

    
avto1=Avto("Gentra","oq","Avtomat","140 000 000 so`m",1,3)
avto2=Avto("Cobalt","oq","Avtomat","120 000 000 so`m",1,3)
avto3=Avto("Malibu","oq","Avtomat","240 000 000 so`m",1,3)


avto4 = Avto("Nexia","oq","Avtomat","100 000 000 so`m",1,3)

salon1 = Avtosalon('UzAvto', 'Uzbekistan')

salon2 = Avtosalon('Sam Avto', 'Samarqand')

salon1.add_car(avto1, avto3)

salon2.add_car(avto2, avto4)

print(salon1.salon_cars())
print(salon1.cars_num)

print(salon2.salon_cars())
print(salon2.cars_num)
        



# UYGA VAZIFA
# O'quvchi klasi (ism, familiyasi, tyil .....)
# Maktab klasi (nomi, oquvchilari, oquvchilar soni)

# 18 --> 3,4,5,6,7,8,9
# 45 --> 3,4,5,6,7,8,9