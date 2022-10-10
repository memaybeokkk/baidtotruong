A, B, C, p, q, r = [int(i) for i in input().split()]
min = min(A/p,B/q,C/r)
print(A/p - min,B-min*q,C- min*r)