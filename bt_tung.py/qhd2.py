s1 = 10
a = [7,6,3,10,4,8]
a = [0] + a
L = [0] * 100
n = len(a)
L[0] = 1
d = [0] * n
SL = 0
max = 0
kt = False
def xuli():
	global SL,L,kt,max
	s = s1
	L = [0] * (s+1);max = 0;L[0] = 1;kt = False
	for i in range(1,n):
		for st in range(max,-1,-1):
			if st + a[i] > s:
				continue
			if L[st] != 0 and L[st+a[i]] == 0 and d[i] == 0:
				L[st+a[i]] = i
				if st + a[i] == s:
					kt = True
					break
				if st + a[i] > max:
					max = st + a[i]		
	while s > 0:
		i = L[s]
		if i>=1:
			print(a[i],end=' ')
			d[i] = 1
			SL = SL + 1
			s = s - a[i]
while SL != n:
	xuli()
	print()
	if not kt:
		break