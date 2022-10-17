a=[3,2,5,1,8,6,3]
a=['j']+a
s1=14
l=[0]*(s1+1)
n=len(a)
d=[0]*100000
def xuli():
	global l,kt,d
	s=s1
	l=[0]*(s+1);tongmax=0;l[0]=1;kt=False
	for i in range(1,n):
		for st in range(tongmax,-1,-1):
			if st+a[i]<=s:
				if l[st+a[i]]==0 and l[st]!=0 and d[i]==0:
					l[st+a[i]]=i
					if st+a[i]==s:
						kt=True
						break
					if st+a[i]>tongmax:
						tongmax=st+a[i]
	if kt==False:
		return ()
	while s>0:
		i=l[s]
		if i>=1:
			print(a[i],end=' ')
			d[i]=1
			s-=a[i]
while True:
	xuli()
	print()
	if kt==False:
		break


	