n = [1,3,12,75,21,100]
m = 19
a = [0]*(50)
a[0]=1;a[1]=1;min=0
for i in range(2,50):
    a[i]=a[i-1]+a[i-2]
    if a[i] < m and a[i]>min:
    	min = i
    if a[i] >m:
    	break
print(m,end='=')
while m != 0 and min >=0:
	if m - a[min] > 0:
		print(a[min],'+',sep='',end='')
		m = m - a[min]
	elif m - a[min] == 0:
		print(a[min],end='')
		break
	min-=1
	
