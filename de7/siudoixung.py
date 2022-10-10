s = 'abacdc'
def doixung(s):
	s = str(s)
	if s == s[::-1]:
		return True
	return False
a = []
def Hoanvi(a, b):
    a, b = b, a
    return (a, b)
for i in range(len(s)):
	for j in range(i+1,len(s)):
		if doixung(s[i:j+1]):
			a.append(s[i:j+1])