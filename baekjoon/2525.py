a,b =map(int, input().split())
c=int(input())

if b+c>=60:
    a += (b+c)//60
    b = (b+c)%60
    if a >=24:
        a = a%24
        print(a, b)
    else: print(a,b)
else:
    print(a,b+c)