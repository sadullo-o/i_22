# UYGA VAZIFA

# import re

# urlandoza = '(?P<url>https?://[^\s]+)'
# matn = 'Ozbekiston respublikasi xalq talim vazirligi websayti: https://www.facebook.com/ '

# saytlar = re.findall(urlandoza, matn)

# print(saytlar)


# Tashqi kutubxonalar
# py -m pip install kutubxonanomi

# googletrans
# py -m pip install googletrans==3.1.0a0
# from googletrans import Translator

# tarjimon = Translator()

# matn = 'Qora mashina chiroyli'

# tarjimaqilingan = tarjimon.translate(matn, src='uz' ,dest='ru')

# print(tarjimaqilingan.text)




# requests  ->internetdan malumotlarni olib beruvchi kutubxona
# py -m pip install requests

import requests

# manzil = 'https://uzedu.uz/uz'

# r = requests.get(manzil)

# print(r.text)

# https://restcountries.com/v3.1/name/{name}

# davlat = input('Davlat nomi>> ')

# manzil = f'https://restcountries.com/v3.1/name/{davlat}'

# r = requests.get(manzil)

# r_oddiy = r.json()[0]

# print(r_oddiy['capital'][0])



# beautifulsoup

# py -m pip install beautifulsoup4

# from bs4 import BeautifulSoup
# import requests

# manzil = 'https://uzedu.uz/uz'
# r = requests.get(manzil)

# s = BeautifulSoup(r.text, 'html.parser')

# # yangiliklar = s.find_all(class_='imageBox')
# info = s.find_all(class_='logoTextBox')
# print(info[0].text)




# wordcloud, matplotlib

# py -m pip install wordcloud
# py -m pip install matplotlib






# py -m pip install fuzzywuzzy


# from fuzzywuzzy import fuzz, process

# # print(fuzz.ratio('bahor', 'anor'))

# soz = 'olma'

# royxat = ['solma', 'anor', 'bolga', 'tolmas']

# t = process.extract(soz, royxat, limit=2)

# bitta = process.extractOne(soz, royxat)

# print(t)

# print(bitta)