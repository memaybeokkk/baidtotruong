f2 = open('Bai5.out','w')
with open('Bai5.inp','r') as f1:
	k = int(f1.readline())
	s = f1.readline()
a = []
d = 0
for i in range(len(s)):
	for j in range(i,len(s)):
		a.append(s[i:j+1])
for i in a:
	if i.count('1') == k:
		d+=1
f2.write(str(d))
f2.close()