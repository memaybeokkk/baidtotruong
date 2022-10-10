n = 5
s = 11
a = [9,2,3,4,1]
t = [0] * (n+1) 
t[1] = a[0]
a = [0] + a
for i in range(1,n+1):
	t[i] = t[i-1] + a[i]
for i in range(1,n+1):
	for j in range(i,n+1):
		if t[j] - t[i-1] >= s:
			if j - i + 1 < n+1:
				print(i,j)
				dem = j - i + 1
				break
print(dem)