a,d = [float(i) for i in input().split()]
n = int(input())
L = n * d + 0.5
s = 0
for i in range(n+1):
	vt = int(i*d/(4*a))
	vt = i*d - 4*a*vt
	if vt <= a:
		print('{:.10f}'.format(float(vt)),'{:.10f}'.format(float(0)))
	elif vt <= 2*a:
		print('{:.10f}'.format(float(a)),'{:.10f}'.format(float(vt-a)))
	elif vt < 3*a:
		print('{:.10f}'.format(float(3*a - vt)),'{:.10f}'.format(float(a)))
	else:
		print('{:.10f}'.format(float(0)),'{:.10f}'.format(float(4*a - vt)))



