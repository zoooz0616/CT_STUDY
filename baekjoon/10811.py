n,m = map(int, input().split())
list=[0]*n
for i in range(n):
    list[i]=i+1
for a in range(m):
    i,j=map(int, input().split())
    new=[]
    for b in range(i-1,j):
        new.append(list[b])
    z=0
    for c in range(j-1, i-2,-1):
        list[c]=new[z]
        z+=1
for i in range(n):
    print(list[i], end=' ')