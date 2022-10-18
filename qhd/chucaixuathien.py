n = 3
X = ['abc1x2y3z','cb1','1cd7hd']
Y = []
for i in range(3):
	t = ''
	for j in range(len(X[i])):
		if '0' <= X[i][j] <= '9':
			t+=X[i][j]
	Y.append(len(t))
print(X,Y)
Z = [i for _,i in sorted(zip(Y,X))]
print(Z)