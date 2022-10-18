n = 3
a = [-1,-1,1]
tp = 0
cs = 0
s = 0
for i in range(n):
	if a[i] <= -1 and s == 0:
		tp+=1
	else:
		s+=a[i]
print(tp)




