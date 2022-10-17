f2 = open('Clan.OUT','w')
with open('Clan.INP','r') as f1:
	s1 = f1.readline()
	s2 = []
	for i in range(int(s1)):
		s2.append(int(f1.readline()))
a = set(s2)
dem = 0
for i in a:
	dem+= s2.count(i)//i
f2.write(str(dem))
f2.close


		
