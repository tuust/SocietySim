import building as b
import person as p
import numpy as np
import math, pyglet
from random import randint
from pyglet import clock
import graphics
from time import sleep

maju = 25
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

# gui aken
window = graphics.simwin(majad, inimesi, resizable=True, width=1280, height=720)

# for rida in range(len(majad)):
#     for maja in range(len(majad[rida])):
#         if isinstance(majad[rida, maja], b.kodu):
#             range(len(majad))
#             if len(inimesed) < kodu-5:
#                 inimarv = randint(2,5)#Mitu inimest elab ühes kodus
#             else:
#                 inimarv = kodu - len(inimesed)
#             for inim in range(inimarv):

# Algsete haigete määramine
pikkus = math.sqrt(maju)-1
koords = []
def inithaige():
    x = randint(0,pikkus)
    if x not in koords:
        koords.append(x)
        window.inimesed[x].staatus = 1
        window.haiged += 1
    else: inithaige()
for i in range(haige):
    inithaige()
window.terved = inimesi - window.haiged

# sim'i mainloop
def elu(dt):
    haiged = []
    for inim in window.inimesed:
        print(inim.aeg)
        if inim.aeg == 10:
            koht = next(inim.kohad)
            inim.aeg = 0
            inim.asukoht = getattr(inim, koht) 
        elif not inim.vx and not inim.vy:
            inim.aeg += 1
            if inim.staatus == 1:
                haiged.append(inim.asukoht)
        
    for inim in window.inimesed:
        if inim.staatus == 1 and not inim.vx and not inim.vy:
            if randint(0,1000) <= 20: #tervenemise protsent
                inim.staatus = 2
                window.tervenenud += 1; window.haiged -= 1
        elif inim.staatus == 0 and inim.asukoht in haiged:
            if randint(0,1000) <= 40: #haigestumise protsent
                inim.staatus = 1
                window.haiged += 1; window.terved -= 1

# gui laadimine
pyglet.clock.schedule_interval(elu, 0.5)
pyglet.app.run()