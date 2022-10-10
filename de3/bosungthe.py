n, x = [int() for i in input().split()]
a = [int() for i in input().split()]
s = abs(sum(a))
print(s//x+s%x)