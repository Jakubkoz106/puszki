import os

import cv2

path = "../tekstWyniki"
myListZdjecia = os.listdir(path)

for tekst in myListZdjecia:
    f = open("../tekstWyniki/"+tekst, "r",encoding="utf8")
    #print(f.read())
    x=f.read()
    klucz = ["Składniki:","SKŁADNIKI:"]
    for i in klucz:
        if i in x:
            print("------------------------------------"+tekst)
            print(x.split(i)[1].split(".")[0])
