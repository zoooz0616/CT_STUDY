n=int(input())
m=int(input())
a=list(map(int, input().split()))
a.sort()
i=0
j=n-1
count=0

while i<j:
    if a[i]+a[j] < m:
        i += 1
    elif a[i] + a[j] > m:
        j -= 1
    else :
        count += 1
        i += 1
        j -= 1
        
print(count)