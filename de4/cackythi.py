x, k = [int(i) for i in input().split()]
d = [0] * x
for i in range(k):
	a = [int(i) for i in input().split()]
	if a[0] == 1:
		d[a[1]] = 1 
		d[a[2]] = 2
	else:
		d[a[1]] = 1
b = []
for i in range(1,x):
	if d[i] == 0:
		b.append(i)
print(b)
dem = len(b)
while j < dem - 1:
	if b[j+1] - b[j] == 1:
		dem = dem - 1 
		j = j + 2
	j + 1

print(dem)