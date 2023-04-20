white=[1,1,2,2,2,8]
black=list(map(int, input().split()))

for i in range(len(white)):
    print(white[i]-black[i], end=' ')