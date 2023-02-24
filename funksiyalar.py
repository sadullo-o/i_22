import random
from sozlar import words


def get_word():
    soz = random.choice(words)
    while '-' in soz or ' ' in soz:
        soz = random.choice(words)

    return soz.upper()

# olma --m-

def display_word(f_sozi, word):
    matn = ''
    for i in word:
        if i in f_sozi:  # ''
            matn += i
        else:
            matn += '-'
        
    return matn


def oynash():
    soz = get_word()
    # soz dagi harflar
    harflar = set(soz)

    # foydalanuvchi kiritgan harflar
    f_harflar = ''

    while harflar:
        print(display_word(f_harflar, soz))  # ----- 


        if f_harflar:
            print(f'Hozirgacha kiritgan harflaringiz: {f_harflar}')
        
        harf = input('Harf kiriting: ').upper()
        if harf in f_harflar:
            print('Bu harfni oldin ham kiritdingiz!!!')
            continue
        elif harf in soz:
            harflar.remove(harf)
            print(f"{harf} harfi togri")
        else:
            print('Bunday harf mavjud emas')

        f_harflar += harf

    print(f"Tabriklaymiz! {soz} so'zini {len(f_harflar)} ta urinishda topdingiz")



