n = 13
d = 1
i = 2
j = 2
while d < n:  
	dem = 0 
	while True:
		if i % j == 0:	
			dem+=1
			d+=1
		if d == n:
			break
		if dem == j:
			break
		i+=1
	if d == n:
		break
	i+=1
	j+=1
print(i)
		