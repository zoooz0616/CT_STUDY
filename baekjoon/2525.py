a,b =map(int, input().split())
c=int(input())

if b+c<60:
    print(a, b+c)
elif b+c>=60:
    if a+1<24:
        if b+c == 120:
            print(a + 2, b + c - 120)
        else: print(a + 1, b + c - 60)
    else: print((a+1-24), (b+c-60))