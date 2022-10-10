a = [int(i) for i in input().split()]
n = a[0]
a[0] = 0
T = [0] * (n+1)
T[0] = a[1]
mina = min(a[1:n])
for i in range(0,n+1):
	T[i] = T[i-1] + a[i]
for i in range(n+1):
	m = abs(T[n] - T[i] - T[i])
	if m < mina:
		mina = m
print(mina)