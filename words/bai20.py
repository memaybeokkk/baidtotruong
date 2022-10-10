n = int(input())
i = 2
print(n,'=',end='')
while n > 1:
    if n % i== 0:
        if n != 1:
             print(i,'*',end='')
        else:
             print(i,end='')
        n = n // i
    else:
        i += 1
