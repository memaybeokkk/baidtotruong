m, n = [int(i) for i in input().split()]
a = []
b = []
for i in range(m):
	nhap = input().lstrip('*')
	if nhap.index('S') < nhap.index('G'):
		a = []
		break
	a.append(nhap.count('*')+ 1)
a = sorted(a)
dem = 0
while a != []:
	min = a[0]
	for i in a:
		if i-min == 0:
			b.append(i)
	for i in b:
		a.pop(a.index(i))
	b = []
	dem+=1
if dem == 0:
	print(-1)
else:
	print(dem)