# So'z topish o'yini. 
from funksiyalar import oynash


while True:
    oynash()
    savol = input('Yana davom ettirasizmi? (ha/yoq)')
    if savol == 'yoq':
        break