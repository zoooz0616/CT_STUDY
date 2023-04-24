c=int(input())

for i in range(c):
    a=list(map(int, input().split()))
    stn = a[0]
    score_list=a[1:stn+1]
    avg=sum(score_list)/stn
    count=0
    for j in score_list:
        if j>avg:
            count+=1
    result=count/stn*100.0
    print(f"{result:.3f}%")