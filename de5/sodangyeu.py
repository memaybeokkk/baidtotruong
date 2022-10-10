n = int(input())
dem = 1
for i in range(1,n//2+1):
	if n % i == 0:
		dem+=1
if n%dem == 0:
	print('dang yeu')