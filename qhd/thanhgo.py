n = 4
a = [2,8,4,6]
def ucln(a,b):
	if a%b == 0:
		return b
	return ucln(b,a%b)
uc = ucln(a[0],a[1])
for i in range(len(a)):
	uc = ucln(uc,a[i])
print(uc)	


