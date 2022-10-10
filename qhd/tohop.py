x=[0]*50;
n=5;k=3
def ghinghiem(x):
	
	for i in range(1,k+1):
		print(x[i],end=' ');
	print()

def tohop(i):
	for j in range(x[i-1]+1,n-k+i+1):
		x[i]=j
		print(x[0:10])
		if i==k: ghinghiem(x)
		else:
			tohop(i+1)
x[0]=0
tohop(1)
