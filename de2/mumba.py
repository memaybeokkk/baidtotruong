def xau(s):
	if s.count('bb') != 0:
		return False
	for i in range(len(s)):
		for j in range(i,len(s)):
			d = j - i + 1
			if s[i:j+1] == s[j+1:j+d+1] == s[j+d+1:j+2*d+1]:
				return False
		if i == len(s)-3*d:
			break
	return True
print(xau('aabababababbb'))