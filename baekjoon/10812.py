n,m=map(int, input().split())
basket=[0]*n
for i in range(len(basket)):
    basket[i]=i+1


for i in range(m):
    begin,end,mid =map(int,input().split())
    basket[mid-1:end],basket[begin-1:mid-1]=basket[begin-1:mid-1],basket[mid-1:end]
for i in basket:
    print(i,end=' ')