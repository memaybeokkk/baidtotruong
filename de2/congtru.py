a = int(input())
phep = intput()
b = int(input())
if phep == 'cong':
	T = a+b
elif phep == 'tru':
	T = a - b 
elif phep == 'nhan': 
	T = a * b
else:
	T = a // b
print(T)
np = ''
while T > 0:
	np+= str(T%2)
	T//=2
print(np[::-1])