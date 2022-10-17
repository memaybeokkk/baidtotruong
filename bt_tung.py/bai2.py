n = int(input())
s = ''
for i in range(1,n+1):
    s+=str(i)
s = list(s)
while len(s) > 1:
    i = 0
    while i < len(s):
        s.pop(i)
        i+=1
    j = 1
    while j < len(s):
        s.pop(j)
        i+=1
s = str(s)
print(s)
