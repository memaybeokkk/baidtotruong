n = 7
m = 3
a = [1,2,2,1,1,3,3]
dapso = n
j = 0
for i in range(n):
	nho = [0] * 1000000
	dem = 0
	while j < n and dem < m:
		j+=1
		nho[a[j]]+=1
		if nho[a[j]] == 1:
			dem+=1
	if dem == m and dapso>j-i+1:
		dapso = j-i+1
		nho[a[i]]-=1
	if nho[a[i]]==0:
		dem-=1
print(dem)
