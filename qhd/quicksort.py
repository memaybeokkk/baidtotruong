a=['2','20','004','66']
n=len(a)
def quickSort(a,L,R):
	i = L 
	j = R 
	x = a[(L+R)//2]
	while i <=j:
		while a[i] + x > x + a[i]:
			i+=1
		while x + a[j] > a[j] + x:
			j-=1
		if i <= j:
			temp = a[i]
			a[i] = a[j]
			a[j] = temp
			i+=1
			j-=1
		if L < i:
			quickSort(a,L,j)
		if j < R:
			quickSort(a,i,R)
quickSort(a,0,n-1)
print(a)
