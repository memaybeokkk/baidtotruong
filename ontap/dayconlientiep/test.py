a=[1,5,3,0,2,1,4,3,6,8]
l=[0]*(len(a))
max=0
for i in range(1,len(a)):
	lmax=0
	for j in range(i-1,-1,-1):
		if a[i]-a[j]==2 and l[j]>lmax:
			lmax=l[j]
	l[i]=lmax+1
	if l[i]>max:
		max=l[i]
print(max)