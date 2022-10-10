n = 20
a = []
for i in range(2,n//2+1):
	if n % i == 0:
		a.append(i)
a.append(n)
max = 0
for i in range(len(a)):
	kt = True
	for j in range(2,a[i]):
		if a[i] % (j**2) == 0:
			kt = False
			break
	if kt == True and a[i] > max:
		max = a[i]
print(max)

