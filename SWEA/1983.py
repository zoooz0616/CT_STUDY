T=int(input())
for i in range(T):
    N,K=map(int, input().split()) #학생 수와 찾고싶은 애
    array = []
    re=0
    index=0
    for j in range(N):
        M, F, G=map(int, input().split())
        score = M*0.35 +F*0.45 + G*0.2
        if j+1 == K:
            re=score
        array.append(score)
    array.sort(reverse=True)

    for j in range(N):
        if array[j]==re:
            index=j
            break
    n=N//10
    s=["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
    print("#{} {}".format(i+1,s[index//n]))
