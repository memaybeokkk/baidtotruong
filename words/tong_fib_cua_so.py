n = int(input())
h = n
s = 0
l = [1,1]
for i in range(0,n):
	if l[i] + l[i+1] > n:
		break
	l.append(l[i] + l[i+1])
print(l)
l = l[::-1]
while h >0:
	
