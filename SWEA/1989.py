T=int(input())
for i in range(1,T+1):
    result=1
    s=list(input())
    for j in range(len(s)//2):
        if s[j]==s[-1-j]:
            continue
        else :
            result=0
            break
    print("#{} {}".format(i,result))