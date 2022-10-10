n = int(input())
def duthua(n):
	s = 0
	for i in range(1,n//2+1):
		if n%i == 0:
			s+=i
	if s > n:
		return True
	return False
while duthua(n) != True:
	n+=1
print(n)
