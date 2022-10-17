a,d = [float(i) for i in input().split()]
n = int(input())
for i in range(1,n+1):
	L = d * i
	k = L%(a*4)
	if k <= a:
		print('{:.10f}'.format(float(k)),'{:.10f}'.format(float(0)))
	elif a < k <= 2*a:
		print('{:.10f}'.format(float(a)),'{:.10f}'.format(float(k-a)))
	elif 2*a < k <= 3*a:
		print('{:.10f}'.format(float(a -(k-2*a))),'{:.10f}'.format(float(a)))
	else:
		print('{:.10f}'.format(float(0)),'{:.10f}'.format(float(a-(k-3*a))))



