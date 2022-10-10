s1 = input()
s2 = input()
l1 = len(s1)
l2 = len(s2)
vtd = []
vtc = []
if l1 < l2:
	temp = s1
	s1 = s2 
	s2 = temp
	temp1 = l1
	l1 = l2 
	l2 = temp1
for i in range(l1):
	for j in range(i,l2):
		if s2[i:j] in s1:
			vtd.append(i)
			vtc.append(j)

for i in range(len(vtd)):
	print(s2[vtd[i]:vtc[i]])
 