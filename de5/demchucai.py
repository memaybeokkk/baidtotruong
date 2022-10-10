s = input()
s = s.lower().split()
s1 = s
s = ''.join(s)
a = [0] * 1000
for i in s:
	a[ord(i)]+=1
for i in range(97,123):
	if a[i] != 0:
		print(chr(i),a[i])
