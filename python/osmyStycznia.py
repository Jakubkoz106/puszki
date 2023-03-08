import os
from PIL import Image

import SzukaniePuchy
path1 = "../zdjecia"

   #sciezka do folderu z zdjeciami puszek


myListZdjecia = os.listdir(path1)

#print(path)

# defaultowe dane dla ktorych jest w miare najlepiej  ilePixeli=11   coKtoreZdjecie=2

ilePixeli = 12 # dane do zabawy   im wiecej tym lepiej ale bez przesady
coKtoreZdjecie=2  # dane do zabawy  im wiecej zdjec tym lepsza jakosc ale dluzej trzeba czekac


max_height = 2000   # dana nie skalowalna do naszych zdjec nie wiem czy do kazdej puchy bedzie pasowac


for zdjecie in myListZdjecia:
    path2 = "../zdjecia/"+zdjecie
    myList360 = os.listdir(path2)
    total_width = int(ilePixeli * len(myList360) / coKtoreZdjecie) + 1  # 1 pixel zapasowy ale nie wiem czy moze sie zdazyc ze bedzie za malo
    new_im = Image.new('RGB', (total_width, max_height - 400))
    x_offset = 0
    top = SzukaniePuchy.minHeight(path2)
    for imgN in myList360[::coKtoreZdjecie]:
        #print(path)
        print(imgN)
        curImg = Image.open(f'{path2}/{imgN}')

        width, height = curImg.size
        left = int(width/2 -100)
        bottom = max_height
        right = int(width/2 - 100)+ilePixeli


        curImg = curImg.crop((left, top, right, bottom))

        new_im.paste(curImg, (x_offset, 0))
        x_offset += curImg.size[0]

    new_im.save(str("../zdjeciaWyniki/")+str(path2.split("/")[-1])+'test'+str(coKtoreZdjecie)+'koma'+str(ilePixeli)+'.jpg')
