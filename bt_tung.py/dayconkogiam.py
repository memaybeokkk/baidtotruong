f2 = open('Dayconkogiam.OUT','w')
with open('Dayconkogiam.INP','r') as f1:
	n = int(f1.readline())
	a = [int(i) for i in f1.readline().split()]
	a = [-99999] + a + [99999]
	print(a)
	s = len(a)
L = [0] * s
L[s-1] = 1
T = [0] * s
print(L,T)
for i in range(s-2,-1,-1):
	jmax = s-1
	for j in range(i+1,s):
		if a[i] < a[j] and L[j] > L[jmax]:
			jmax = j
	L[i] = L[jmax] + 1
	T[i] = jmax

print(L,T)
f2.write(str(L[0]-2))
f2.write('\n')
i = T[0]
while i != s-1:
	f2.write(str(a[i]))
	f2.write(' ')
	i = T[i]
f2.close()