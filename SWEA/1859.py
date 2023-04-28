t=int(input())
for i in range(t):
    result=0
    num=int(input())
    price =list(map(int,input().split()))
    array=[0]*num
    itemMax = price[-1]

    for j in range(num-2,-1,-1):
        if price[j]<itemMax:
            array[j]=itemMax-price[j]
        else:
            itemMax=price[j]
    print("#{} {}".format((i+1),sum(array)))
