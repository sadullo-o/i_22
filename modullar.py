def kopaytma(*sonlar):
    natija = 1
    for i in sonlar:
        natija *= i
    
    return natija



def lugatt(ism_familiya ,**lugat):
    lugat['F.I.O']=ism_familiya
    return lugat


def lugat_yarat(til ,**lugat):
    lugat['lang'] = til
    return lugat


PI = 3.1415

PAROL = 'safkby7eb3u3873yb'