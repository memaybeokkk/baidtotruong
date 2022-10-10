# XAU CON CHUNG DAI NHAT
s1='019012304'
s2='0034012'
m=len(s1);n=len(s2)
L=[0]*n
for i in range(n):
    L[i]=[0]*m

for i in range(1,n):
               for j in range(1,m):
                   if s2[i]==s1[j]:
                       L[i][j]=L[i-1][j-1]+1
                   else:
                       L[i][j]=max(L[i][j-1],L[i-1][j])
print('do dai xau con chung dai nhat',L[n-1][m-1])
GTLN=L[n-1][m-1]
 # Truy vét
csd=[];csc=[]
for j in range(m):
    if L[n-1][j]==L[n-1][m-1]:
        
         csd.append(n-1)
         csc.append(j)
print(csd,csc)
dmax=0
for k in range(len(csd)):
    
    i=csd[k]
    j=csc[k]
    c=''

    while (i!=0) and (j!=0):
        if s2[i]==s1[j]:
          c=s2[i]+c
          i=i-1;
          j=j-1;
        elif L[i][j]==L[i-1][j]:
           i=i-1
           
        else:
          j=j-1
    print(c)
    if dmax<int(c):
       dmax=int(c)
print(dmax)         
 
       
   
  
 
