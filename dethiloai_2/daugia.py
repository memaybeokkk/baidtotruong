from math import sqrt
snt = [True] * 100900
can_n=int(100001**0.5)+1
snt[0] = snt[1] = False
for i in range(2,can_n+1):
	if snt[i] == True:
		for j in range(i*i,100001,i):
			snt[j] = False
a, b = [int(i) for i in input().split()]
d = 0
for i in range(a,b+1):
	xau = str(i)
	if snt[i] == True and xau == xau[::-1]:
		d+=1
print(d)

