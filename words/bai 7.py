import time
tb = time.time()
a = str(999999)
s = [int(i) for i in a.split()]
print(sum(s))
print(time.time()- tb)
