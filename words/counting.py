n = input()
a = ['0','1','2','3','4','5','6','7','8','9']
for i in a:
    dem = n.count(i)
    if dem != 0:
        print(i,':',dem)
