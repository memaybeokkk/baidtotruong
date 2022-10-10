def sdt(n):
    s = 0;kt= False
    for i in range(1,n//2+1):
        if n%i ==0:
            s += i
        if s>n:
            kt=True
    return kt

for i in range(0,10000):
    if sdt(i):
        print(i)
        break
