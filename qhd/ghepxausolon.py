a=['2','20','004','66']
n=len(a)
def sapxep(a, L, R):
	i = L
	j = R
	x = a[(L + R)//2]

	while (i<=j):
		while a[i]+x>x+a[i]:
			i = i+1

		while a[j]+x<x+a[j]:
			j = j - 1
 
		if i <= j:
			tg=a[i]
			a[i]=a[j]
			a[j]=tg
			i+=1 
			j-=1


		if L<j:
			sapxep(a,L, j)
		if i<R:
			sapxep(a,i, R)
sapxep(a, 0, n - 1)

print("Day so khi duoc sap xep la: ", a)