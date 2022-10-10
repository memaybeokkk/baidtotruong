n = [int(i) for i in input().split()]
a = []
d = 0
for i in range(len(n)):
	for j in range(i,len(n)):
		if n[i] != n[j] and n[j] not in a:
			a.append(n[j])
			d+=1
print(d,a,sep='\n')