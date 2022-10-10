n = int(input())
d = 0
def ucln(a,b):
	if a%b == 0:
		return b
	return ucln(b,a%b)
for i in range(1,n):
	if ucln(i,20) == 1:
		d+=1
print(d)