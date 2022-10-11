a = [0] * 50
n = [4,1,1,7,10,8]
a[0] = a[1] = 1 
i = 2 
d = 0
a = [0]*(50)
a[0]=1;a[1]=1;max = max(n)
for i in range(2,50):
    a[i]=a[i-1]+a[i-2]
    if a[i] in n:
    	d+=1
    if a[i] > max:
    	break
if 1 in n:
	d+=1
print(d)