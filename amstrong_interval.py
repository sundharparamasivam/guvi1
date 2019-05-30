s=list(input().split())
v=0
l=[]
l1=[]
for a in range(int(s[0])+1,int(s[1])):
    a=str(a)
    for i in a:
        c=int(i)**len(a)
        v=v+c
       # continue
    if a==str(v):
        l.append(a)
    else:
        l1.append(a)
    v=0
print(*l)
