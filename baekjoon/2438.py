n=int(input())
for i in range(1,n+1):
    s=""
    for j in range(n-i):
        s+=" "
    for k in range(i):
        s+="*"
    print(s)