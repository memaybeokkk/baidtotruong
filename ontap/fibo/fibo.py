n = [1,3,12,75,21,100]
m = 22
a = [0]*(50)
a[0]=1;a[1]=1;min=0
for i in range(2,50):
    a[i]=a[i-1]+a[i-2]
    if a[i] < m and a[i]>min:
    	min = a[i]
print(a[0:50])


