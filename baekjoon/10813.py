n, m = map(int,input().split())
basket = [0]*n
for i in range(n):
    basket[i]=i+1
for a in range(m):
    i, j = map(int, input().split())
    temp=basket[i-1]
    basket[i-1]=basket[j-1]
    basket[j-1]=temp
for i in range(n):
    print(basket[i], end=' ')