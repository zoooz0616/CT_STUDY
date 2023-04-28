T=int(input())
for i in range(T):
    array = list(map(int, input().split()))
    result=0
    for j in array:
        if(j%2==1):
            result+=j
    print("#{} {}".format((i+1),result))