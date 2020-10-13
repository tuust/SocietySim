import person as p
import building as b
import virus as v
import numpy as np
import pyglet as pl
#import graphics as gui
import math
from random import randint
print("Proovi test2")

#inimene = int(input("sisestage inimeste arv:"))
#haige = int(input("sisestage haigete arv:"))
#surnud = int(input("sisestage suremisprotsent:"))
#surnud = round(haige / 100)
#haige = haige - l2
#terved = inimene - haige
#lo = [ka, l3, l2]
#print(terved)
##haige = (haige * 2)  
majad = []
maju = 100
for x in range(int(math.sqrt(maju))):
    majad.append([])
koole = maju * 0.02
haiglad = maju * 0.01
haiglad = int(haiglad)
koole = int(koole)
for maja in range(maju - haiglad - koole):
    i = randint(0,int(math.sqrt(maju)) - 1)
    
    majad[i].append(b.kodu)
    
#print(majad)
inimesed = []
for haiglaid in range(haiglad):
    h = haiglad
    majad[h].append(b.haigla)
print(majad)


while True:
    break
