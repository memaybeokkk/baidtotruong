n = int(input())
i = 1
dem = 0
def mayman(x):
	while x > 0:
		if x%10 == 3 or x % 10 == 5 :
			x=x//10
		else:
			return False
	return True
gtmu = 1
while i < 100000:
	if gtmu >= n:
		mu = i
		break
	else:
		dem+=(2**i)
		gtmu+=(2**i)
		i+=1
for i in range(10**(mu-1),10**mu):
	if mayman(i):
		dem+=1
		if dem == n:
			print(i)
			break
