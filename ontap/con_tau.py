s1=6
a=[4,2,1,5,5]
a=[0]+a 
n=len(a)
d=[0]*(n)
SL = 0
dem=0
def xuli():
	global SL,L,kt
	s=s1;tmax=0
	L=[0]*(s+1); maxtong=0;L[0]=1;kt=False
	for i in range(1, n):
		for st in range(maxtong,-1,-1):
			if st+a[i]>s:
				continue
			if (L[st]!=0) and (L[st+a[i]]==0) and d[i]==0:
				L[st+a[i]]=i
				if st+a[i]>maxtong:
				   maxtong=st+a[i]
		if tmax<maxtong:
			tmax=maxtong
	s=tmax
	print('max=',s)
	while s>0 : 
		i=L[s]
		if i>=1:
			print(a[i],' ',end=' ')
			d[i]=1
			SL=SL+1
			s=s-a[i]
while SL!=n-1: 
	xuli()
	print()
	dem=dem+1
print('so lan',dem)