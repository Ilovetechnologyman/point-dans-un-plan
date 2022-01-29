print("ce programme permet de savoir si un point appartient a un plan")
print("entrez coordone dun point")
pointx = int(input('entrez x'))
pointy = int(input('entrez y'))
pointz = int(input('entrez z'))
print("entrez les coef de equa cartesienne")
plana = int(input("entrez a"))
planb = int(input("entrez b"))
planc = int(input("entrez c"))
pland = int(input("entrez d"))
equation = plana*pointx + planb*pointy + planc*pointz + pland

if equation == 0 :
    print("le point appartient au plan !")
else:
    print("le point n'appartient pas au plan!")
