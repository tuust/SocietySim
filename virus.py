import person as p
class koroona:
    def __init__(self):
        pass

def kList(mList): 
	 
	r = 1
	for x in mList: 
		r = r * x 
	return r
ka = int(input("sisestage inimeste arv:"))
l1 = int(input("sisestage haigete arv:"))
l2 = int(input("sisestage suremisprotsent:"))
l2 = round(l2 / 100)
l1 = l1 - l2
l1 = [l1, 3]  
print(kList(l1))
l3 = str(ka)
l3 = int(l3)
l3 = (int(ka) - int(l1)- int(l2)
#lo = [ka, l3, l2]
#print(l3)