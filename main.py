import building as b
import person as p
import numpy as np
import math
from random import randint
#inimene = int(input("sisestage inimeste arv:"))
#haige = int(input("sisestage haigete arv:"))
#surnud = int(input("sisestage suremisprotsent:"))
#surnud = round(haige / 100)
#haige = haige - l2
#terved = inimene - haige
#lo = [ka, l3, l2]
#print(terved)
##haige = (haige * 2)
maju = 100
majad = np.array([])

koole = int(maju * 0.02)
majad = np.append(majad, np.full((1,koole), b.kool()))

haiglad = int(maju * 0.01)
majad = np.append(majad, np.full((1,haiglad), b.haigla()))

kodu = maju - haiglad - koole
majad = np.append(majad, np.full((1,kodu), b.kodu()))

# ja teiste majadega ka


# teeb majad mitmedimensiooniliseks ja ajab majad segamini
np.random.shuffle(majad)
majad = np.reshape(majad, (int(math.sqrt(maju)),int(math.sqrt(maju))))

#print(majad)
#inimesed

inimesed = {'vanur':[],}
inimesed = {'tooline':[],}
inimesed = {'tootu':[],}
inimesed = {'opilane':[],}
for rida in range(len(majad)):
    for maja in range(len(majad[rida])):
        if isinstance(majad[rida, maja], b.kodu):
            print('kodu')
            range(len(majad))
            inimene = p.vanur()
            inimene.kodu = [rida, maja]#koordinaadid
            inimene.asukoht = [rida, maja]
            inimesed['vanur'].append(inimene)
            inimene = p.tootu()
            inimesed['tootu'].append(inimene)
            inimene = p.tooline()
            inimesed['tooline'].append(inimene)
            inimene = p.opilane()
            inimesed['opilane'].append(inimene)



