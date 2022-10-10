n = int(input())
a = [int(i) for i in input().split()]
a = a[0:n]
i = 0
dmin = cuoi = n
'''
dau = 0
for i in range(0,n-2):
	if a[i] ==1 and a[i+1] == 0:
		dau = i + 1
	if a[i] == 0 and a[i+1] == 1:
		cuoi = i
		if dmin > cuoi - dau +1:
			dmin = cuoi - dau + 1
print(dmin)
'''
while i < n - 2:
	if a[i] == 1 and a[i+1] == 0 and i < n - 2:
		d = 1
		while a[i+1] == a[i+2] == 0 and i < n - 3:
			d = d + 1
			i = i + 1
		if d < dmin:
			dmin = d

	else:
		i+=1

print(dmin)