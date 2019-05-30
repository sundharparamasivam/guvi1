su=list(map(int,input().split()))
for i in range(su[0]+1,su[1]):
    for j in range(2,i):
        if i%j==0:
            break    
    else:
        print(i,end=" ")
