n=int(input())
list=list(map(int, input().split()))
m=0
for i in range(n):
    if list[i]>m:
        m=list[i]
avg=sum(list)/m*100/n
print(avg)