n = int(input())
T = 0
while n > 0:
    du = n%10
    n = n//10
    T = T + du**2
print(T)

