# imtihon tahlili
import json


class Shifoxona:
    def __init__(self, nomi):
        self.nomi = nomi
        self.bemorlar = []
        self.bemorlar_soni = 0
        self.tuzalganlar_soni = 0

    def bemor_qoshish(self, bemor):
        self.bemorlar.append(bemor)
        self.bemorlar_soni += 1
        bemor.shifoxona = self
        
        
        with open('bemorlar.json') as fayl:
            try:
                bemorlar = json.load(fayl)
            except:
                bemorlar = []
            bemorlar.append({
                'FIO': bemor.FIO,
                'kasallik': bemor.kasallik,
                'bòlim': bemor.bòlim
            })
            with open('bemorlar.json', 'w') as f:
                json.dump(bemorlar, f)


    def tuzalish(self, bemor):
        self.tuzalganlar_soni += 1
        with open('bemorlar.json') as f:
            bemorlar1 = json.load(f)
            n = 0
            for i in bemorlar1:
                if i['FIO'] == bemor.FIO:
                    del bemorlar1[n]
                n+=1
            

        with open('bemorlar.json', 'w') as f:
            json.dump(bemorlar1, f)

        with open('tuzalganlar.json') as f:
            try:
                tuzalganlar = json.load(f)
            except:
                tuzalganlar = []
            tuzalganlar.append({
                'Shifoxona': self.nomi,
                'Bemor': bemor.FIO
            })
        with open('tuzalganlar.json', 'w') as f:
            json.dump(tuzalganlar, f)


class Bemor:
    def __init__(self, FIO, kasallik, bòlim):
        self.FIO = FIO
        self.kasallik = kasallik
        self.bòlim = bòlim
        self.shifoxona = None

    def tuzalish(self):
        if self.shifoxona is not None:
            self.shifoxona.tuzalish(self)



shaharshifo = Shifoxona('24-poliklinika')

bemor1 = Bemor('Ali Valiyev', 'grip', 'yuqumli kasalliklar')
bemor2 = Bemor('Hasan Husanov', 'covid', 'yuqumli kasalliklar')
bemor3 = Bemor('Rustam Boltayev', 'covid', 'yuqumli kasalliklar')

# shaharshifo.bemor_qoshish(bemor1)
# shaharshifo.bemor_qoshish(bemor2)
# shaharshifo.bemor_qoshish(bemor3)


shaharshifo.tuzalish(bemor1)

