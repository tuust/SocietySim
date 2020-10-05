class koroona:
    def __init__(self):
        pass

def kList(mList): 
	 
	r = 1
	for x in mList: 
		r = r * x 
	return r
l = int(input("sisestage haigete arv:"))
list1 = [l, 3]  
print(kList(list1))