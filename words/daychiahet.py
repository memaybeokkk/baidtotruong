n = int(input())
j = 1
dem = 0
for i in range(1,100001):
	dem2 = 0
	while dem2 < i:
		if j%i == 0:
			dem+=1
			dem2+=1
			j+=i
		else:
			j+=1
	if dem == n:
		print(j-i)
		break


