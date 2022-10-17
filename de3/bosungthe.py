n, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
s = abs(sum(a))
print(s//x+s%x)
print(s//x,s%x)