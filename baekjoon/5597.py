list=[0]*30
for i in range(28):
    n=int(input())
    list[n-1]=1

for i in range(30):
    if list[i]==0:
        print(i+1)