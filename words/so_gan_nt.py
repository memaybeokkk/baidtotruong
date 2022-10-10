n = int(input())
a = [True] * 1000000
a[0] = a[1] = False
for i in range(2,1000000):
	if a[i] == True:
		if i*i>=n:
			print(i*i)
			break
		for j in range(2,10//i):
			a[i*j] = False
