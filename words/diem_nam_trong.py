xA, yA, xC, yC, xM, yM, xN, yN = [int(i) for i in input().split()]
if xA > xC and yA > yC:
	temp = xA
	xA = xC
	xC = temp
	temp1 = yA
	yA = yC
	yC = temp1
elif yA > yC:
	temp2 = xA
	xA = xC
	xC = temp2
	temp3 = yA
	yA = yC
	yC = temp3
if xA < xM < xC and yA < yM < yC:
	print(2)
elif xA < xM < xC or yA < yM < yC:
	print(1)
elif  xM >= xC > xA or yM >= yC > yA:
	print(0)