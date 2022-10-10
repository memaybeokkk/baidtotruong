a = [0,3,2,5,1,8,6,3]
s = sum(a)
n = len(a)
L = [0] * (n+1)
Tmax = 0
L[0] = 1
s =s// 2
while s != 0:
	kt = False
	for i in range(1,n):
		for st in range(Tmax,-1,-1):
			if st + a[i] <= s:
				if L[st] != 0 and L[st+a[i]] ==0:
					L[st+a[i]] = i
					if st + a[i] == s:
						kt = True
						break
					if st + a[i] > Tmax:
						Tmax = st + a[i]
	if kt == True:
		while s > 0:
			if i >= 1:
				i = L[s]
				print(a[i],' ',end=' ')
				b[i] = 1
				s = s - a[i]
	s-=1
print()
for i in range(1,n):
	if b[i] == 0:
		print(a[i],end=' ')