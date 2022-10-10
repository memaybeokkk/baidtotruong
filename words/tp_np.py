n = int(input())
a =[]
while n > 0:
    a.append(n%2)
    n=n//2
a.reverse()
b = ''.join(a)
print(b)
