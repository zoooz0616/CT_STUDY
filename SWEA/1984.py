T=int(input())
for i in range(1,T+1):
    array = list(map(int,input().split()))
    array.remove(max(array))
    array.remove(min(array))
    result=sum(array)/len(array)
    print("#{} {}".format(i,round(result)))