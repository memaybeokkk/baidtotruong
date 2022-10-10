from math import sqrt
snt = [True] * 100000
snt[0] = snt[1] = False
for i in range(2,int(sqrt(100000))):
	if snt[i] == True:
		for j in range(i,100000//i):
			snt[i*j] = False
print(snt[0:100])
s = 'timpassword232432fsdgd45435dsfdsf'
t = ''
for i in range(len(s)):
	if '0' <= s[i] <= '9':	
		t = t + s[i]
max = 0
for i in range(len(t)):
	for j in range(i,i+5):
		if snt[int(t[i:j+1])]:
			if int(t[i:j+1]) > max:
				max = int(t[i:j+1])


print(max)


