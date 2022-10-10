s = input()
a = [True] * len(s)
b = [True] * len(s)
d1 = 0
d2 = 0
for i in range(len(s)-1):
	if s[i] != s[i+1] and a[i] == a[i+1] == True:
		d1+=1
		a[i] = a[i+1] = False
		print(a)

if s[0] != s[-1]:
	d+=1
	b[0] = b[-1] = False
for i in range(len(s)-1):
	if s[i] != s[i+1] and b[i] == b[i+1] == True:
		d2+=1
		b[i] = b[i+1] = False
		print(b)
if d1
print(d,a)

