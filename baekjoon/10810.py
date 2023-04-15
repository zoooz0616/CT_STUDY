list=[]
n, m = map(int, input().split())
for a in range(m):
    i,j,k = map(int, input().split())
    for i in range(j+1):
        list[i-1]=k
print(list)