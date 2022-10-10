from ngaythang import songay
s = '311198'
s1 = s[:-2]
if len(s1) == 4:
	if int(s1[-2:]) <= 12:
		day = songay(s[-2:],'20' + s[-2:])
		if int(s[:2]) <= day:
			print(s[:2],'-',s[2:4],'-','20' + s[-2:])
if len(s1) == 3:
	if int(s1[-2:]) <= 12:
		day = songay(s[-1:],'20' + s[-2:])
		if int(s[-1:]) <= day:
			print(s[0],'-',s[1:3],'-','20' + s[-2:])
			print(s[:2],'-',s[1:2],'-','20' + s[-2:])
if len(s1) == 2:
	print(s[0],'-',s[1],'-','20' + s[-2:])
else:
	print('KHONG')






	
	

