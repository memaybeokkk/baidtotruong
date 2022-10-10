#cach 1
"""
n = int(input())
s = []
for i in range(n):
	s.append(input())
for i in s:
	if i == i[::-1]:
		print('CO')
	else:
		print('KHONG')
"""
#cach 2
f = open('xaudoixung.OUT','w')
def xaudx(s):
	kt = True
	s = s.rstrip('\n')
	for i in range(len(s)//2+1):
		if s[i] != s[len(s)-i-1]:
			kt = False
	return kt
with open('xaudoixung.INP','r') as tep1:
	n = int(tep1.readline())
	for i in range(n):
		if xaudx(tep1.readline()):
			f.write('CO')
			f.write('\n')
		else:
			f.write('KHONG')
			f.write('\n')
f.close()