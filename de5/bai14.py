n = int(input())
s = input()
def doixung(s):
	s = str(s)
	if s == s[::-1]:
		return True
	return False
dmax = 0
vtd = []
vtc = []
for i in range(n):
	for j in range(i,n):
		if doixung(s[i:j]):
			if len(s[i:j]) > dmax:
				dmax = len(s[i:j])
				vtd = [i]
				vtc = [j]
			elif len(s[i:j]) > dmax:
				vtd.append(i)
				vtc.append(j)
for i in range(len(vtd)):
	print(s[vtd[i]:vtc[i]])

