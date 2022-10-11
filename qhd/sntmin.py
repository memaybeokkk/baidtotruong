n = [3,8,5,1,2,12,9]
from math import sqrt
snt = [True] * 1000001
can_n=int(1000001**0.5)+1
snt[0] = snt[1] = False
for i in range(2,can_n+1):
	if snt[i] == True:
		for j in range(i*i,1000001,i):
			snt[j] = False
i = 2
d = 0
print(snt[0:10])
while True:
	if i not in n and snt[i] == True:
		print(i)
		break
	i+=1
