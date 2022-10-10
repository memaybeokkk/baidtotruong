m, n = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
vt = 0
dem = 0
a.sort()
b.sort()
for i in range(len(a)):
	for j in range(vt,len(b)):
		if a[i] > a[j]:
			vt = j
			dem+=1
			print(i,j)
			break
print(dem)