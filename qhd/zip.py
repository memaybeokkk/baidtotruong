def nen(s):
	t = ''
	for i in range(len(s)):
		if s[i] not in t:
			if s.count(s[i]) > 1:
				t = t + str(s.count(s[i])) + s[i]
			else:
				t = t + s[i]
	return t

def giainen(s):
	t = ''
	cs = ['1','2','3','4','5','6','7','8','9']
	for i in range(0,len(s),1):
		if s[i] in cs:
			t = t + str(int(s[i])*s[i+1])
	return t
print(giainen('ab3cd2e'))
