# o'zgaruvchilar, royxatlar (list, tuple, set, dict), if else, foor, while, funksiyalar, random

import random

def sontop_odam(x=15):
    taxminiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} oraliqda taxminiy son o'yladim, toping?")
    taxminlar = 0
    while True:
        taxminlar += 1
        odam_son = int(input('>>'))
        if odam_son<taxminiy_son:  # 9 --> 3
            print('Xato, men oylagan son bundan katta')
        elif odam_son>taxminiy_son: 
            print('Xato, men oylagan son bundan kichik')  # 9  --> 14
        else:
            break
    
    print(f"Tabriklaymiz. Siz {taxminlar} ta taxmin bilan topdingiz")
    return taxminlar


def sontop_komp(x=15):
    input(f"1 dan {x} gacha oraliqda bitta son o'ylang va men uni topaman>>")
    min = 1
    max = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if min != max:  # 13
            taxmin = random.randint(min, max)  # 6
        else:
            taxmin = min
        javob = input(f"Siz {taxmin} sonini o'yladingiz. togri (t), men uyagan son katta (+), men uylagan son kichik(-)")
        if javob == '-':
            max = taxmin - 1
        elif javob == '+':
            min = taxmin + 1
        elif javob == 't':
            break
        else:
            continue
    
    print(f"Men {taxminlar} ta taxmin bilan topdim")
    return taxminlar


def play(x=15):
    yana = True
    while yana:
        urinish_odam = sontop_odam(x)
        urinish_komp = sontop_komp(x)

        if urinish_odam > urinish_komp:
            print(f"Men {urinish_komp} ta urinish bilan golib boldim")
        elif urinish_odam < urinish_komp:
            print(f"Siz {urinish_odam} ta urinish bilan golib bo'ldinigiz")
        else:
            print('Durrang boldi')
        savol = input('Yana uynaysizmi? ha/yoq')
        if savol == 'yoq':
            yana = False
        else:
            yana = True

