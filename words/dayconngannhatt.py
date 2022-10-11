n = 6
d = 11
a = [0,1,2,3,4,5]
T = [0] * n
T[0] = a[0]
min = n+1
csd = []
csc = []
for i in range(1,n):
	T[i] = T[i-1] + a[i]
for i in range(n):
	for j in range(i,n):
		if T[j] - T[i-1] >= d and j-i+1<min:
			min = j - i + 1
			break
print(min)

