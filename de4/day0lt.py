n = int(input())
a = []
for i in range(n):
	a.append(int(input()))
i = 0
max = 0
while i < n:
	dem = 0
	while a[i] == 0 and i < n:
		dem+=1
		i+=1
		if i >= n:
			break
	if dem >= max:
		max = dem
	i+=1
	if i >= n:
		break
print(max)