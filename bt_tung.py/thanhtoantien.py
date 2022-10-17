n = int(input())
k = [int(i) for i in input().split()]
d = 1000000
for i in range(n):
    m = [int(i) for i in input().split()]
    time = 0
    time = sum(m) * 5 + len(m) * 15
    if time < d:
        d = time
print(d)
