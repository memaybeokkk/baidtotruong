n = int(input())
F = [1,1]
i = 1
while F[i] < n:
    F.append(F[i] + F[i-1])
    i+=1
F.pop(-1)
print(F)
i = len(F) - 1
while n != 0 and i >= 0:
    if n - F[i] >0:
        print(F[i],'',end='')
        n = n - F[i]
    elif n - F[i] ==0:
        print(F[i])
        n = n - F[i]
    i-=1
        

    
