n, k = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
d = 0
for i in range(n):
	if 5 - y[i] >= k:
		d+=1
print(d//3)