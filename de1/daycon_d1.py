n, s = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
T = [0] * n
for i in range(1,n):
	T[i] = T[i-1] + a[i]
dem = n
for i in range(n):
	for j in range(i,n):
		if T[j] - T[i-1] >= s:
			if j - i + 1 <= dem:
				dem = j - i + 1
				break
print(dem)
