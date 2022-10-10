n = int(input())
a = [int(i) for i in input().split()]
a = a[0:n]
D = [0] * 100000
dmax = 0
max = 0
for i in a:
	D[i]+=1
	if D[i] > dmax:
		dmax = D[i]
		max = i
	elif D[i] == dmax:
		if i < max:
			max = i
print(max,dmax)