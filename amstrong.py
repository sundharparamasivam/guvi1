a=input()
v=0
for i in a:
    c=int(i)**len(a)
    v=v+c
    continue
if a==str(v):
    print("yes")
else:
    print("no")
