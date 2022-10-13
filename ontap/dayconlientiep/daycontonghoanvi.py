m = 9
n = 10
a = [4,6,5,1,9,10,5,2,4]
k = 0
luu = [0] * 100
tong = 0 
def In():
	for i in range(k):
		print(luu[i],end=' ')
	print()
def tim(i):
	global tong,k
	if tong == n:
		In()
	else:
		for j in range(m):
			if tong+a[j] <= n and j>i:
				tong = tong+a[j]
				k = k + 1
				luu[k] = a[j]
				tim(j)
				k = k - 1
				tong = tong - a[j]
for i in range(m):
	tim(a[i])
	k = 0
	tong = 0
