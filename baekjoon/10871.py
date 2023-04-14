n,x = map(int, input().split())
a=input().split()
s=""
for i in range(n):
    if int(a[i])<x:
        s += a[i]+" "
print(s)

