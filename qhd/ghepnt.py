from math import sqrt
snt = [True] * 1000000
snt[0] = snt[1] = False
L = []
k = 5
for i in range(2,int(sqrt(1000000))):
	if snt[i]:
		for j in range(i*i,1000000//2,i):
			snt[j] = False
for i in range(len(snt)):
	if snt[i]:
		L.append(i)
dem = 0
i = 1
while dem != k:
	s = str(L[i-1]) + str(L[i])
	if snt[int(s)]:
		dem+=1
	i+=1
print(s)
