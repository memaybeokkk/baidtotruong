with open('SUMN.INP','r') as tep1:
	s = tep1.readline()
T = 0
for i in s:
	T = T + int(i)
with open('SUMN.OUT','w') as tep2:
	tep2.write(str(T))
