a = [int(i) for i in input().split()]
n = len(a)
D = [0] * 100000 
f = [0]*100
f[0,1] = 1,1
dem = 0
for i in range(2,n+1):
    f[i]=f[i-1]+f[i-2]
for i in a:
	if f.count(i) != 0 and D[i] = 0:
		dem = dem + 1
		D[i] = 1
print(dem)