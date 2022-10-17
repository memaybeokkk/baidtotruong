f2 = open('Virus.out','w')
with open('Virus.inp','r') as f1:
	k,n = [int(i) for i in f1.readline().split()]
	a = []
	dem = 0
	for i in range(0,k):
		s1 = f1.readline()
		a.append(s1.rstrip('\n'))
	print(a)
	for j in range(n):		
		s2 = f1.readline()
		d=0
		while d != k:
			d = 0
			for i in a: 
				s2 = s2.replace(i,'')
				dem+=1
			for i in a:
				if s2.find(i) == -1:
					d+=1	
		print(s2)

f2.write(str(dem))

f2.close()