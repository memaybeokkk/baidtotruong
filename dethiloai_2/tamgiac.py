from math import *
xA, yA =  [int(i) for i in input().split()]
xB, yB =  [int(i) for i in input().split()]
xC, yC =  [int(i) for i in input().split()]
xD, yD =  [int(i) for i in input().split()]
def dttg(xA, yA, xB, yB, xC, yC):
	t = abs((xB-xA)*(yC-yA)-(xC-xA)*(yB-yA))
	Sabc = 1/2*(t)
	return Sabc
if (xD == xA and yD == yA) or (xD == xB and yD == yB) or (xD == xC and yD == yC):
	print(1)
else:
	if dttg(xA, yA, xB, yB, xD, yD) + dttg(xB, yB, xC, yC, xD, yD) + dttg(xA, yA, xC, yC, xD, yD) == dttg(xA, yA, xB, yB, xC, yC):
		print(1)
	else:
		print(0)