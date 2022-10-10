a = input()
S = []
dem = 0
for i in range(len(a)):
	for j in range(i,len(a)):
		print(S)
		if S.count(a[i:j+1]) == 0:
			S.append(a[i:j+1])
			dem+=1

print(S,dem)