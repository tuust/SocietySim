import building as b
import person as p
import numpy as np
import math
from random import randint
from itertools import cycle
from pyglet import clock

maju = 100
majad = np.array([])

# koole = int(maju * 0.02)
# majad = np.append(majad, np.full((1,koole), b.kool()))

# haiglad = int(maju * 0.01)
# majad = np.append(majad, np.full((1,haiglad), b.haigla()))

# pood = int(maju * 0.02)
# majad = np.append(majad, np.full((1,poed), b.pood()))


kodu = maju #- haiglad - koole# - pood - kontor
majad = np.append(majad, np.full((1,kodu), b.kodu()))



# teeb majad mitmedimensiooniliseks ja ajab majad segamini
np.random.shuffle(majad)
majad = np.reshape(majad, (int(math.sqrt(maju)),int(math.sqrt(maju))))
#print(majad)
#inimesed
inimesi = kodu*3 #populatsiooni arvutamine

haige = 3
terved = inimesi - haige

inimesed = []
pikkus = math.sqrt(maju)
for rida in range(len(majad)):
    for maja in range(len(majad[rida])):
        if isinstance(majad[rida, maja], b.kodu):
            range(len(majad))
            if len(inimesed) < kodu-5:
                inimarv = randint(2,5)#Mitu inimest elab ühes kodus
            else:
                inimarv = kodu - len(inimesed)
            for inim in range(inimarv):
                
                # inimese loomine
                inim = p.tooline()
                inim.staatus = 0    #Terved(0), Haiged(1), Tervenenud(2)
                inim.kodu = [rida, maja] #Inimese kodu kordinaadid
                i = math.sqrt(maju)
                inim.too = [randint(0,pikkus),randint(0,pikkus)]
                inim.pood = [randint(0,pikkus),randint(0,pikkus)]
                inim.asukoht = [rida, maja] #Kus inimene asub
                inimesed.append(inim)

# Algsete haigete määramine
koords = []
def inithaige():
    x = randint(0,pikkus)
    if x not in koords:
        koords.append(x)
        inimesed[x].staatus = 1
    else: inithaige()
for i in range(haige):
    inithaige()

kohad = cycle(iter(['too', 'pood', 'kodu']))
while True:
    haiged = []
    koht = next(kohad)
    for inim in inimesed:
        inim.asukoht = getattr(inim, koht) 
        if inim.staatus == 1:
            haiged.append(inim.asukoht)
        
    for inim in inimesed:
        if randint(0,100) <= 10: #tervenemise protsent
            inim.staatus = 2
        if inim.asukoht in haiged:
            if randint(0,100) <= 40 and inim.staatus != 2: #haigestumise protsent
                inim.staatus = 1
