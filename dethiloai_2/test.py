"""def sieve(n):
    danh_dau=[True]*(n+1) 
    can_n=int(n**0.5)+1
    for i in range(2,can_n+1):
        if danh_dau[i]:           
            for j in range(i*i,n+1,i):
                danh_dau[j]=False
    primes=[]
    for i in range(2,n+1):
        if danh_dau[i]:
            primes.append(i)
    return primes"""

a = [3] * 10000
print(a)