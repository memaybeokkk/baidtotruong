from math import *
x1 = int(input())
y1 = int(input())
R1 = int(input())
x2 = int(input())
y2 = int(input())
R2 = int(input())
l = sqrt((x1-x2)**2 + (y1-y2)**2)
if l == 0:
	kc = abs(R1-R2)
elif l == R1 + R2:
	kc = 0
elif l > R1 + R2:
	kc = l - R1 - R2
else:
	if l < R1:
		kc = R1 - l - R2
	elif l < R2:
		kc = R2 - l - R1
	else:
		kc = 0
print('{:.3f}'.format(float(kc)))