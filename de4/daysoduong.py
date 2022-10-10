n = int(input())
a = [int(i) for i in input().split()]
T = [0] * n
T[0] = a[0]
for i in range(1,n):
	T[i] = T[i-1] + a[i]
T = [0] + T
for i in range(1,n+1):
	for j in range(i,n+1):
		if T[j] - T[i-1] > 0:
			print(i,j)
			