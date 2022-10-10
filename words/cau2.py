a,b = [int(i) for i in input('').split()]
T = 0
for i in range(len(str(a))):
    for j in range(len(str(b))):
        T += a[i] * b[j]
print(T)
                   
                
