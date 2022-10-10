sb = 'truongnguyendu'
se = 'nguyenduquannhat'
i = 0
j = 0
for i in range(len(sb)):
	if sb[i:] == se[:len(sb[i:])]:
		vt = len(sb) - i
		break
s = sb + se[vt:]
print(s,len(s))



